# Generated from SQL.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SQLParser import SQLParser
else:
    from SQLParser import SQLParser

# This class defines a complete listener for a parse tree produced by SQLParser.
class SQLListener(ParseTreeListener):

    # Enter a parse tree produced by SQLParser#pocket.
    def enterPocket(self, ctx:SQLParser.PocketContext):
        pass

    # Exit a parse tree produced by SQLParser#pocket.
    def exitPocket(self, ctx:SQLParser.PocketContext):
        pass


    # Enter a parse tree produced by SQLParser#statement.
    def enterStatement(self, ctx:SQLParser.StatementContext):
        pass

    # Exit a parse tree produced by SQLParser#statement.
    def exitStatement(self, ctx:SQLParser.StatementContext):
        pass


    # Enter a parse tree produced by SQLParser#create.
    def enterCreate(self, ctx:SQLParser.CreateContext):
        pass

    # Exit a parse tree produced by SQLParser#create.
    def exitCreate(self, ctx:SQLParser.CreateContext):
        pass


    # Enter a parse tree produced by SQLParser#insert.
    def enterInsert(self, ctx:SQLParser.InsertContext):
        pass

    # Exit a parse tree produced by SQLParser#insert.
    def exitInsert(self, ctx:SQLParser.InsertContext):
        pass


    # Enter a parse tree produced by SQLParser#delete.
    def enterDelete(self, ctx:SQLParser.DeleteContext):
        pass

    # Exit a parse tree produced by SQLParser#delete.
    def exitDelete(self, ctx:SQLParser.DeleteContext):
        pass


    # Enter a parse tree produced by SQLParser#select.
    def enterSelect(self, ctx:SQLParser.SelectContext):
        pass

    # Exit a parse tree produced by SQLParser#select.
    def exitSelect(self, ctx:SQLParser.SelectContext):
        pass


    # Enter a parse tree produced by SQLParser#columnNames.
    def enterColumnNames(self, ctx:SQLParser.ColumnNamesContext):
        pass

    # Exit a parse tree produced by SQLParser#columnNames.
    def exitColumnNames(self, ctx:SQLParser.ColumnNamesContext):
        pass


    # Enter a parse tree produced by SQLParser#values.
    def enterValues(self, ctx:SQLParser.ValuesContext):
        pass

    # Exit a parse tree produced by SQLParser#values.
    def exitValues(self, ctx:SQLParser.ValuesContext):
        pass


    # Enter a parse tree produced by SQLParser#constants.
    def enterConstants(self, ctx:SQLParser.ConstantsContext):
        pass

    # Exit a parse tree produced by SQLParser#constants.
    def exitConstants(self, ctx:SQLParser.ConstantsContext):
        pass


    # Enter a parse tree produced by SQLParser#expressionList.
    def enterExpressionList(self, ctx:SQLParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by SQLParser#expressionList.
    def exitExpressionList(self, ctx:SQLParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by SQLParser#booleanExpression.
    def enterBooleanExpression(self, ctx:SQLParser.BooleanExpressionContext):
        pass

    # Exit a parse tree produced by SQLParser#booleanExpression.
    def exitBooleanExpression(self, ctx:SQLParser.BooleanExpressionContext):
        pass


    # Enter a parse tree produced by SQLParser#compare.
    def enterCompare(self, ctx:SQLParser.CompareContext):
        pass

    # Exit a parse tree produced by SQLParser#compare.
    def exitCompare(self, ctx:SQLParser.CompareContext):
        pass


    # Enter a parse tree produced by SQLParser#expression.
    def enterExpression(self, ctx:SQLParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SQLParser#expression.
    def exitExpression(self, ctx:SQLParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SQLParser#identifier.
    def enterIdentifier(self, ctx:SQLParser.IdentifierContext):
        pass

    # Exit a parse tree produced by SQLParser#identifier.
    def exitIdentifier(self, ctx:SQLParser.IdentifierContext):
        pass


    # Enter a parse tree produced by SQLParser#constant.
    def enterConstant(self, ctx:SQLParser.ConstantContext):
        pass

    # Exit a parse tree produced by SQLParser#constant.
    def exitConstant(self, ctx:SQLParser.ConstantContext):
        pass


    # Enter a parse tree produced by SQLParser#fileIdentifier.
    def enterFileIdentifier(self, ctx:SQLParser.FileIdentifierContext):
        pass

    # Exit a parse tree produced by SQLParser#fileIdentifier.
    def exitFileIdentifier(self, ctx:SQLParser.FileIdentifierContext):
        pass



del SQLParser