# Generated from SQL.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,34,158,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,4,0,35,8,0,11,0,12,0,36,1,0,1,0,1,1,
        1,1,1,1,1,1,3,1,45,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,5,3,61,8,3,10,3,12,3,64,9,3,1,4,1,4,1,4,1,4,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,3,5,77,8,5,1,6,1,6,1,6,1,6,5,6,83,8,6,10,6,
        12,6,86,9,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,5,8,97,8,8,10,8,
        12,8,100,9,8,1,9,1,9,1,9,5,9,105,8,9,10,9,12,9,108,9,9,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,5,10,121,8,10,10,10,
        12,10,124,9,10,1,11,1,11,1,12,1,12,1,12,3,12,131,8,12,1,13,1,13,
        1,13,1,13,3,13,137,8,13,1,14,1,14,1,14,3,14,142,8,14,1,14,1,14,3,
        14,146,8,14,1,14,1,14,4,14,150,8,14,11,14,12,14,151,3,14,154,8,14,
        1,15,1,15,1,15,0,1,20,16,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,0,2,2,0,19,19,23,27,1,0,21,22,163,0,34,1,0,0,0,2,44,1,0,0,0,4,
        46,1,0,0,0,6,51,1,0,0,0,8,65,1,0,0,0,10,69,1,0,0,0,12,78,1,0,0,0,
        14,89,1,0,0,0,16,93,1,0,0,0,18,101,1,0,0,0,20,109,1,0,0,0,22,125,
        1,0,0,0,24,130,1,0,0,0,26,136,1,0,0,0,28,153,1,0,0,0,30,155,1,0,
        0,0,32,35,3,2,1,0,33,35,5,1,0,0,34,32,1,0,0,0,34,33,1,0,0,0,35,36,
        1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,38,1,0,0,0,38,39,5,0,0,1,
        39,1,1,0,0,0,40,45,3,4,2,0,41,45,3,6,3,0,42,45,3,8,4,0,43,45,3,10,
        5,0,44,40,1,0,0,0,44,41,1,0,0,0,44,42,1,0,0,0,44,43,1,0,0,0,45,3,
        1,0,0,0,46,47,5,2,0,0,47,48,5,5,0,0,48,49,3,30,15,0,49,50,3,12,6,
        0,50,5,1,0,0,0,51,52,5,6,0,0,52,53,5,7,0,0,53,54,5,5,0,0,54,55,3,
        30,15,0,55,56,3,12,6,0,56,57,5,8,0,0,57,62,3,14,7,0,58,59,5,15,0,
        0,59,61,3,14,7,0,60,58,1,0,0,0,61,64,1,0,0,0,62,60,1,0,0,0,62,63,
        1,0,0,0,63,7,1,0,0,0,64,62,1,0,0,0,65,66,5,12,0,0,66,67,5,5,0,0,
        67,68,3,30,15,0,68,9,1,0,0,0,69,70,5,3,0,0,70,71,3,18,9,0,71,72,
        5,4,0,0,72,73,5,5,0,0,73,76,3,30,15,0,74,75,5,11,0,0,75,77,3,20,
        10,0,76,74,1,0,0,0,76,77,1,0,0,0,77,11,1,0,0,0,78,79,5,17,0,0,79,
        84,3,26,13,0,80,81,5,15,0,0,81,83,3,26,13,0,82,80,1,0,0,0,83,86,
        1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,87,1,0,0,0,86,84,1,0,0,0,
        87,88,5,18,0,0,88,13,1,0,0,0,89,90,5,17,0,0,90,91,3,16,8,0,91,92,
        5,18,0,0,92,15,1,0,0,0,93,98,3,28,14,0,94,95,5,15,0,0,95,97,3,28,
        14,0,96,94,1,0,0,0,97,100,1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,
        17,1,0,0,0,100,98,1,0,0,0,101,106,3,24,12,0,102,103,5,15,0,0,103,
        105,3,24,12,0,104,102,1,0,0,0,105,108,1,0,0,0,106,104,1,0,0,0,106,
        107,1,0,0,0,107,19,1,0,0,0,108,106,1,0,0,0,109,110,6,10,-1,0,110,
        111,3,26,13,0,111,112,3,22,11,0,112,113,3,24,12,0,113,122,1,0,0,
        0,114,115,10,2,0,0,115,116,5,28,0,0,116,121,3,20,10,3,117,118,10,
        1,0,0,118,119,5,29,0,0,119,121,3,20,10,2,120,114,1,0,0,0,120,117,
        1,0,0,0,121,124,1,0,0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,21,1,
        0,0,0,124,122,1,0,0,0,125,126,7,0,0,0,126,23,1,0,0,0,127,131,5,16,
        0,0,128,131,3,26,13,0,129,131,3,28,14,0,130,127,1,0,0,0,130,128,
        1,0,0,0,130,129,1,0,0,0,131,25,1,0,0,0,132,133,5,33,0,0,133,134,
        5,14,0,0,134,137,5,33,0,0,135,137,5,33,0,0,136,132,1,0,0,0,136,135,
        1,0,0,0,137,27,1,0,0,0,138,154,5,13,0,0,139,154,3,26,13,0,140,142,
        7,1,0,0,141,140,1,0,0,0,141,142,1,0,0,0,142,143,1,0,0,0,143,154,
        5,31,0,0,144,146,7,1,0,0,145,144,1,0,0,0,145,146,1,0,0,0,146,147,
        1,0,0,0,147,154,5,32,0,0,148,150,5,30,0,0,149,148,1,0,0,0,150,151,
        1,0,0,0,151,149,1,0,0,0,151,152,1,0,0,0,152,154,1,0,0,0,153,138,
        1,0,0,0,153,139,1,0,0,0,153,141,1,0,0,0,153,145,1,0,0,0,153,149,
        1,0,0,0,154,29,1,0,0,0,155,156,3,26,13,0,156,31,1,0,0,0,16,34,36,
        44,62,76,84,98,106,120,122,130,136,141,145,151,153
    ]

class SQLParser ( Parser ):

    grammarFileName = "SQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'.'", "','", "'*'", "'('", "')'", "'='", 
                     "'!'", "'-'", "'+'", "'>'", "'>='", "'<'", "'<='", 
                     "'!='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "CREATE", "SELECT", "FROM", 
                      "FILE", "INSERT", "INTO", "ROWS", "UPDATE", "SET", 
                      "WHERE", "DELETE", "NULL", "DOT", "COMMA", "ASTERISK", 
                      "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", "EQUALS", 
                      "NOT", "MINUS", "PLUS", "GT", "GE", "LT", "LE", "NE", 
                      "AND", "OR", "QUOTED_STRING", "INTEGER_VALUE", "DECIMAL_VALUE", 
                      "IDENTIFIER", "WS" ]

    RULE_pocket = 0
    RULE_statement = 1
    RULE_create = 2
    RULE_insert = 3
    RULE_delete = 4
    RULE_select = 5
    RULE_columnNames = 6
    RULE_values = 7
    RULE_constants = 8
    RULE_expressionList = 9
    RULE_booleanExpression = 10
    RULE_compare = 11
    RULE_expression = 12
    RULE_identifier = 13
    RULE_constant = 14
    RULE_fileIdentifier = 15

    ruleNames =  [ "pocket", "statement", "create", "insert", "delete", 
                   "select", "columnNames", "values", "constants", "expressionList", 
                   "booleanExpression", "compare", "expression", "identifier", 
                   "constant", "fileIdentifier" ]

    EOF = Token.EOF
    T__0=1
    CREATE=2
    SELECT=3
    FROM=4
    FILE=5
    INSERT=6
    INTO=7
    ROWS=8
    UPDATE=9
    SET=10
    WHERE=11
    DELETE=12
    NULL=13
    DOT=14
    COMMA=15
    ASTERISK=16
    LEFT_PARENTHESIS=17
    RIGHT_PARENTHESIS=18
    EQUALS=19
    NOT=20
    MINUS=21
    PLUS=22
    GT=23
    GE=24
    LT=25
    LE=26
    NE=27
    AND=28
    OR=29
    QUOTED_STRING=30
    INTEGER_VALUE=31
    DECIMAL_VALUE=32
    IDENTIFIER=33
    WS=34

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class PocketContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SQLParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.StatementContext)
            else:
                return self.getTypedRuleContext(SQLParser.StatementContext,i)


        def getRuleIndex(self):
            return SQLParser.RULE_pocket

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPocket" ):
                listener.enterPocket(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPocket" ):
                listener.exitPocket(self)




    def pocket(self):

        localctx = SQLParser.PocketContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_pocket)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 34
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2, 3, 6, 12]:
                    self.state = 32
                    self.statement()
                    pass
                elif token in [1]:
                    self.state = 33
                    self.match(SQLParser.T__0)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 36 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4174) != 0)):
                    break

            self.state = 38
            self.match(SQLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def create(self):
            return self.getTypedRuleContext(SQLParser.CreateContext,0)


        def insert(self):
            return self.getTypedRuleContext(SQLParser.InsertContext,0)


        def delete(self):
            return self.getTypedRuleContext(SQLParser.DeleteContext,0)


        def select(self):
            return self.getTypedRuleContext(SQLParser.SelectContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = SQLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.create()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.insert()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.delete()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 43
                self.select()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CreateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CREATE(self):
            return self.getToken(SQLParser.CREATE, 0)

        def FILE(self):
            return self.getToken(SQLParser.FILE, 0)

        def fileIdentifier(self):
            return self.getTypedRuleContext(SQLParser.FileIdentifierContext,0)


        def columnNames(self):
            return self.getTypedRuleContext(SQLParser.ColumnNamesContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_create

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreate" ):
                listener.enterCreate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreate" ):
                listener.exitCreate(self)




    def create(self):

        localctx = SQLParser.CreateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_create)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(SQLParser.CREATE)
            self.state = 47
            self.match(SQLParser.FILE)
            self.state = 48
            self.fileIdentifier()
            self.state = 49
            self.columnNames()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InsertContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INSERT(self):
            return self.getToken(SQLParser.INSERT, 0)

        def INTO(self):
            return self.getToken(SQLParser.INTO, 0)

        def FILE(self):
            return self.getToken(SQLParser.FILE, 0)

        def fileIdentifier(self):
            return self.getTypedRuleContext(SQLParser.FileIdentifierContext,0)


        def columnNames(self):
            return self.getTypedRuleContext(SQLParser.ColumnNamesContext,0)


        def ROWS(self):
            return self.getToken(SQLParser.ROWS, 0)

        def values(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.ValuesContext)
            else:
                return self.getTypedRuleContext(SQLParser.ValuesContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_insert

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInsert" ):
                listener.enterInsert(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInsert" ):
                listener.exitInsert(self)




    def insert(self):

        localctx = SQLParser.InsertContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_insert)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(SQLParser.INSERT)
            self.state = 52
            self.match(SQLParser.INTO)
            self.state = 53
            self.match(SQLParser.FILE)
            self.state = 54
            self.fileIdentifier()
            self.state = 55
            self.columnNames()
            self.state = 56
            self.match(SQLParser.ROWS)
            self.state = 57
            self.values()
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 58
                self.match(SQLParser.COMMA)
                self.state = 59
                self.values()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeleteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DELETE(self):
            return self.getToken(SQLParser.DELETE, 0)

        def FILE(self):
            return self.getToken(SQLParser.FILE, 0)

        def fileIdentifier(self):
            return self.getTypedRuleContext(SQLParser.FileIdentifierContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_delete

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDelete" ):
                listener.enterDelete(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDelete" ):
                listener.exitDelete(self)




    def delete(self):

        localctx = SQLParser.DeleteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_delete)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(SQLParser.DELETE)
            self.state = 66
            self.match(SQLParser.FILE)
            self.state = 67
            self.fileIdentifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(SQLParser.SELECT, 0)

        def expressionList(self):
            return self.getTypedRuleContext(SQLParser.ExpressionListContext,0)


        def FROM(self):
            return self.getToken(SQLParser.FROM, 0)

        def FILE(self):
            return self.getToken(SQLParser.FILE, 0)

        def fileIdentifier(self):
            return self.getTypedRuleContext(SQLParser.FileIdentifierContext,0)


        def WHERE(self):
            return self.getToken(SQLParser.WHERE, 0)

        def booleanExpression(self):
            return self.getTypedRuleContext(SQLParser.BooleanExpressionContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_select

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelect" ):
                listener.enterSelect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelect" ):
                listener.exitSelect(self)




    def select(self):

        localctx = SQLParser.SelectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_select)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(SQLParser.SELECT)
            self.state = 70
            self.expressionList()
            self.state = 71
            self.match(SQLParser.FROM)
            self.state = 72
            self.match(SQLParser.FILE)
            self.state = 73
            self.fileIdentifier()
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 74
                self.match(SQLParser.WHERE)
                self.state = 75
                self.booleanExpression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnNamesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PARENTHESIS(self):
            return self.getToken(SQLParser.LEFT_PARENTHESIS, 0)

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(SQLParser.IdentifierContext,i)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(SQLParser.RIGHT_PARENTHESIS, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_columnNames

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnNames" ):
                listener.enterColumnNames(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnNames" ):
                listener.exitColumnNames(self)




    def columnNames(self):

        localctx = SQLParser.ColumnNamesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_columnNames)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(SQLParser.LEFT_PARENTHESIS)
            self.state = 79
            self.identifier()
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 80
                self.match(SQLParser.COMMA)
                self.state = 81
                self.identifier()
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 87
            self.match(SQLParser.RIGHT_PARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValuesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PARENTHESIS(self):
            return self.getToken(SQLParser.LEFT_PARENTHESIS, 0)

        def constants(self):
            return self.getTypedRuleContext(SQLParser.ConstantsContext,0)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(SQLParser.RIGHT_PARENTHESIS, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_values

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValues" ):
                listener.enterValues(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValues" ):
                listener.exitValues(self)




    def values(self):

        localctx = SQLParser.ValuesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_values)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(SQLParser.LEFT_PARENTHESIS)
            self.state = 90
            self.constants()
            self.state = 91
            self.match(SQLParser.RIGHT_PARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constant(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.ConstantContext)
            else:
                return self.getTypedRuleContext(SQLParser.ConstantContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_constants

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstants" ):
                listener.enterConstants(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstants" ):
                listener.exitConstants(self)




    def constants(self):

        localctx = SQLParser.ConstantsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_constants)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.constant()
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 94
                self.match(SQLParser.COMMA)
                self.state = 95
                self.constant()
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SQLParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_expressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionList" ):
                listener.enterExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionList" ):
                listener.exitExpressionList(self)




    def expressionList(self):

        localctx = SQLParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.expression()
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 102
                self.match(SQLParser.COMMA)
                self.state = 103
                self.expression()
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # BooleanExpressionContext
            self.operator = None # Token
            self.right = None # BooleanExpressionContext

        def identifier(self):
            return self.getTypedRuleContext(SQLParser.IdentifierContext,0)


        def compare(self):
            return self.getTypedRuleContext(SQLParser.CompareContext,0)


        def expression(self):
            return self.getTypedRuleContext(SQLParser.ExpressionContext,0)


        def booleanExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.BooleanExpressionContext)
            else:
                return self.getTypedRuleContext(SQLParser.BooleanExpressionContext,i)


        def AND(self):
            return self.getToken(SQLParser.AND, 0)

        def OR(self):
            return self.getToken(SQLParser.OR, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_booleanExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanExpression" ):
                listener.enterBooleanExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanExpression" ):
                listener.exitBooleanExpression(self)



    def booleanExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SQLParser.BooleanExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_booleanExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.identifier()
            self.state = 111
            self.compare()
            self.state = 112
            self.expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 122
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 120
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = SQLParser.BooleanExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_booleanExpression)
                        self.state = 114
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 115
                        localctx.operator = self.match(SQLParser.AND)
                        self.state = 116
                        localctx.right = self.booleanExpression(3)
                        pass

                    elif la_ == 2:
                        localctx = SQLParser.BooleanExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_booleanExpression)
                        self.state = 117
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 118
                        localctx.operator = self.match(SQLParser.OR)
                        self.state = 119
                        localctx.right = self.booleanExpression(2)
                        pass

             
                self.state = 124
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CompareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(SQLParser.EQUALS, 0)

        def GT(self):
            return self.getToken(SQLParser.GT, 0)

        def GE(self):
            return self.getToken(SQLParser.GE, 0)

        def LT(self):
            return self.getToken(SQLParser.LT, 0)

        def LE(self):
            return self.getToken(SQLParser.LE, 0)

        def NE(self):
            return self.getToken(SQLParser.NE, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_compare

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompare" ):
                listener.enterCompare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompare" ):
                listener.exitCompare(self)




    def compare(self):

        localctx = SQLParser.CompareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_compare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 260571136) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASTERISK(self):
            return self.getToken(SQLParser.ASTERISK, 0)

        def identifier(self):
            return self.getTypedRuleContext(SQLParser.IdentifierContext,0)


        def constant(self):
            return self.getTypedRuleContext(SQLParser.ConstantContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = SQLParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expression)
        try:
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.match(SQLParser.ASTERISK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.identifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 129
                self.constant()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.IDENTIFIER)
            else:
                return self.getToken(SQLParser.IDENTIFIER, i)

        def DOT(self):
            return self.getToken(SQLParser.DOT, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)




    def identifier(self):

        localctx = SQLParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_identifier)
        try:
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.match(SQLParser.IDENTIFIER)
                self.state = 133
                self.match(SQLParser.DOT)
                self.state = 134
                self.match(SQLParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.match(SQLParser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NULL(self):
            return self.getToken(SQLParser.NULL, 0)

        def identifier(self):
            return self.getTypedRuleContext(SQLParser.IdentifierContext,0)


        def INTEGER_VALUE(self):
            return self.getToken(SQLParser.INTEGER_VALUE, 0)

        def MINUS(self):
            return self.getToken(SQLParser.MINUS, 0)

        def PLUS(self):
            return self.getToken(SQLParser.PLUS, 0)

        def DECIMAL_VALUE(self):
            return self.getToken(SQLParser.DECIMAL_VALUE, 0)

        def QUOTED_STRING(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.QUOTED_STRING)
            else:
                return self.getToken(SQLParser.QUOTED_STRING, i)

        def getRuleIndex(self):
            return SQLParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)




    def constant(self):

        localctx = SQLParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.match(SQLParser.NULL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 139
                self.identifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21 or _la==22:
                    self.state = 140
                    _la = self._input.LA(1)
                    if not(_la==21 or _la==22):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 143
                self.match(SQLParser.INTEGER_VALUE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21 or _la==22:
                    self.state = 144
                    _la = self._input.LA(1)
                    if not(_la==21 or _la==22):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 147
                self.match(SQLParser.DECIMAL_VALUE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 149 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 148
                        self.match(SQLParser.QUOTED_STRING)

                    else:
                        raise NoViableAltException(self)
                    self.state = 151 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FileIdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # IdentifierContext

        def identifier(self):
            return self.getTypedRuleContext(SQLParser.IdentifierContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_fileIdentifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFileIdentifier" ):
                listener.enterFileIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFileIdentifier" ):
                listener.exitFileIdentifier(self)




    def fileIdentifier(self):

        localctx = SQLParser.FileIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_fileIdentifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            localctx.name = self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[10] = self.booleanExpression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def booleanExpression_sempred(self, localctx:BooleanExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         




