#coding=utf-8
import os
import pandas
from pandas import DataFrame
from tabulate import tabulate
from antlr4 import *
from antlr4.CommonTokenStream import CommonTokenStream
from SQLLexer import SQLLexer
from SQLParser import SQLParser
from SQLListener import SQLListener


# https://medium.com/@sasidharc/build-sql-parser-using-antlr4-part1-2044916a8406
# https://medium.com/@sasidharc/build-sql-parser-using-antlr4-part2-1f8cdb011721
class MotleyQLParser(SQLListener):

    def __init__(self, base_path):
        self.tokens = None
        self.base_path = base_path

    def parse(self, sql: str):
        print(f"Parsing SQL: {sql}")
        data = InputStream(sql)
        lexer = SQLLexer(data)
        stream = CommonTokenStream(lexer)
        self.tokens = stream
        parser = SQLParser(stream)
        tree = parser.pocket()
        walker = ParseTreeWalker()
        walker.walk(self, tree)

    def exitCreate(self, ctx: SQLParser.CreateContext):
        file_name = ctx.fileIdentifier().getText()
        column_names_list = ctx.columnNames().identifier()
        column_names = [column_name.getText() for column_name in column_names_list]
        dataframe = DataFrame(columns=column_names)
        print(f"Saving to {self.base_path}/{file_name}")
        dataframe.to_csv(f"{self.base_path}/{file_name}", index=False)

    def exitInsert(self, ctx: SQLParser.InsertContext):
        file_name = ctx.fileIdentifier().getText()
        if not os.path.exists(f"{self.base_path}/{file_name}"):
            raise FileNotFoundError(f"{self.base_path}/{file_name}")
        df = pandas.read_csv(f"{self.base_path}/{file_name}")
        column_names_list = ctx.columnNames().identifier()
        rows_list = ctx.values()
        for row_values in rows_list:
            column_values = row_values.constants().constant()
            line = []
            if len(column_names_list) != len(column_values):
                raise RuntimeError("column to Values mismatch")
            for column_value in column_values:
                line.append(column_value.getText())
            df.loc[len(df.index)] = line

        df.to_csv(f"{self.base_path}/{file_name}", index=False)

    def exitSelect(self, ctx: SQLParser.SelectContext):
        file_name = ctx.fileIdentifier().getText()
        if not os.path.exists(f"{self.base_path}/{file_name}"):
            raise FileNotFoundError(f"{self.base_path}/{file_name}")
        df = pandas.read_csv(f"{self.base_path}/{file_name}")
        bool_exp = ctx.booleanExpression()
        if bool_exp is not None:
            expression = self.tokens.getText(bool_exp.start, bool_exp.stop)
            df = df.query(expression)
        expression_list_ctx = ctx.expressionList()
        expression_list = expression_list_ctx.expression()
        if len(expression_list) == 1 and expression_list[0].getText() == '*':
            print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))
        else:
            new_df = df[[exp.getText() for exp in expression_list]]
            print(tabulate(new_df, headers='keys', tablefmt='psql', showindex=False))

    def exitDelete(self, ctx: SQLParser.DeleteContext):
        file_name = ctx.fileIdentifier().getText()
        file_path = f"{self.base_path}/{file_name}"
        if os.path.exists(file_path):
            os.remove(file_path)


def take_input():
    base_dir = "./test"
    print(base_dir)
    sql = ""
    parser = MotleyQLParser(base_dir)
    while True:
        line = input("$ ").strip()
        sql += line
        if line == 'exit':
            break
        elif line[-1] == ';':
            try:
                parser.parse(sql)
            except FileNotFoundError as e:
                print(f"File Not found at {e}")
            except RuntimeError as e:
                print(f"Error {e} while executing")
            except Exception as e:
                print(f"Error while parsing {e}")
            else:
                sql = ""


if __name__ == '__main__':
    take_input()