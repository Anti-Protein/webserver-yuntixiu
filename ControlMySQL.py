# -*- coding: UTF-8 -*-
import MySQLdb
import MySQLdb.cursors

#MySQL操作类
class ControlMySQL(object):
    
    # 类初始化
    def __init__(self,host,user,passwd,db):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db

    # 建立连接
    def connectdb(self):
        self.database = MySQLdb.connect(host = self.host,
                                        user = self.user,
                                        passwd = self.passwd,
                                        db = self.db,
                                        charset = 'utf8',
                                        # 加上这一句可以使返回值变为字典类型
                                        cursorclass = MySQLdb.cursors.DictCursor
                                        ) #utf8
        # 获取操作游标
        self.cursor = self.database.cursor()

    # 关闭连接
    def closedb(self):
        self.cursor.close()
        self.database.close()

    # 输出结果(查询操作)
    def printresult(self,sql):
        self.connectdb()
        self.cursor.execute(sql)
        
        result = self.cursor.fetchall()
        self.closedb()
        return result

    # 更新数据(修改操作)
    def updata(self,sql):
        self.connectdb()
        try:
            # 执行SQL语句
            linenum = self.cursor.execute(sql)
            
            # 执行修改数据操作一定要commit，否则无法修改服务器端的数据
            self.database.commit() 
            self.cursor.fetchall()
        except:
            # 发生错误回滚事务
            self.database.rollback()
        self.closedb()
        return linenum
    
    # 查询当前数据库的编码集
    def getcharacter(self):
        self.printresult("show variables like 'character%'")
