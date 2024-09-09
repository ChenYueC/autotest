import pymysql
import logging


class Sql_DataBase:
    host = '192.168.110.52'
    port = 3306

    # 链接数据库
    @classmethod
    def connect(cls, database):
        connect = pymysql.connect(host=Sql_DataBase.host, port=Sql_DataBase.port, user='root',
                                  password='root',
                                  database=database, charset='utf8')
        return connect

    # 查询方法
    @classmethod
    def search_tools(cls, database, statement):
        cursor = None
        try:
            cursor = Sql_DataBase.connect(database).cursor()
            cursor.execute(statement)
            search_result = cursor.fetchall()
            print(search_result)
            logging.info(search_result)
            # return search_result
        except Exception as e:
            print(f'{statement}语句、执行失败!', e)
            # logging.info(f'{statement}语句、执行失败!', e)
        finally:
            cursor.close()

    # 执行方法
    @classmethod
    def execute_tools(cls, database, statement):
        cursor = None
        connect = None
        try:
            connect = Sql_DataBase.connect(database)
            cursor = connect.cursor()
            cursor.execute(statement)
            connect.commit()
            print('事务执行成功!', end='')
            # logging.info(statement, '语句执行成功!')
        except Exception as e:
            print(e)
            print(f"{statement}语句,执行失败!进行数据回滚!")
            # logging.info(e)
            # logging.info(f"{statement}语句,执行失败!进行数据回滚!")
            connect.rollback()
        finally:
            cursor.close()
            connect.close()


if __name__ == '__main__':
    # Sql_DataBase().search_tools("explore", 'SELECT id from explore_meeting WHERE meeting_title = "pytest_有局1"')
    Sql_DataBase().execute_tools("explore", "UPDATE explore_meeting SET meeting_status = '01'  WHERE id = '1632556247892918274';")