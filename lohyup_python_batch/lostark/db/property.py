import pymysql


class LostArkDbConfig:
    host = "localhost"
    user = "root"
    password = "wpdns1290!"
    charset = "utf8"
    port = 3306

    def get_connection(self):
        return pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            charset=self.charset,
            port=3306
        )
