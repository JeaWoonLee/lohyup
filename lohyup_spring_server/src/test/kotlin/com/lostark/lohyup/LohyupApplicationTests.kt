package com.lostark.lohyup

import org.apache.ibatis.session.SqlSessionFactory
import org.junit.jupiter.api.Test
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.boot.test.context.SpringBootTest
import org.springframework.context.ApplicationContext

@SpringBootTest
class LohyupApplicationTests @Autowired constructor(
    private val context: ApplicationContext,
    private val sessionFactory: SqlSessionFactory
    ){

    @Test
    fun contextLoads() {
    }

    @Test
    fun testByApplicationContext() {
        try {
            println("=====================")
            println(context.getBean("sqlSessionFactory"))
            println("=====================")
        } catch (e : Exception) {
            e.printStackTrace()
        }
    }

    @Test
    fun testBySqlSessionFactory() {
        try {
            println("=====================")
            println(sessionFactory.toString())
            println("=====================")
        } catch (e : Exception) {
            e.printStackTrace()
        }
    }
}
