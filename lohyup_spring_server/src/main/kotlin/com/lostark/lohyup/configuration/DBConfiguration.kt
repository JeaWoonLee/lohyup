package com.lostark.lohyup.configuration

import com.zaxxer.hikari.HikariConfig
import com.zaxxer.hikari.HikariDataSource
import org.apache.ibatis.session.SqlSessionFactory
import org.mybatis.spring.SqlSessionFactoryBean
import org.mybatis.spring.SqlSessionTemplate
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.boot.context.properties.ConfigurationProperties
import org.springframework.context.ApplicationContext
import org.springframework.context.annotation.Bean
import org.springframework.context.annotation.Configuration
import org.springframework.context.annotation.PropertySource
import javax.sql.DataSource

@Configuration
@PropertySource("classpath:/application.properties")
class DBConfiguration {

    @Autowired
    private lateinit var applicationContext: ApplicationContext


    /**
     * Hikari Connection Pool 설정
     * Connection Pool 라이브러리
     *
     * 커넥션 객체를 생성해두고, 데이터베이스에 접근하는 사용자에게 미리 생성해둔 커넥션을 제공했다가 다시 돌려받는 방법
     */
    @Bean
    @ConfigurationProperties(prefix = "spring.datasource.hikari")
    fun hikariConfig(): HikariConfig = HikariConfig()

    /**
     * DataSource
     * Connection Pool 을 지원하기 위한 인터페이스
     */
    @Bean
    fun datasource(): DataSource = HikariDataSource(hikariConfig())

    /**
     * SqlSessionFactory
     * 데이터베이스의 커넥션과 SQL 실행에 대한 모든 것을 가짐
     *
     * SqlSessionFactoryBean 은 Mybatis 와 Spring 의 연동 모듈로 사용
     * Mybatis XML Mapper, 설정 파일 위치 등을 지정하고, SqlSessionFactoryBean 자체가 아닌,
     * getObject 메서드가 리턴하는 SqlSessionFactory 를 생성
     */
    @Bean
    fun sqlSessionFactory(): SqlSessionFactory? {
        val factoryBean = SqlSessionFactoryBean()
        factoryBean.setDataSource(datasource())

        return factoryBean.`object`
    }

    /**
     * SqlSession
     *
     * SqlSession For Mybatis
     * 1. SqlSessionTemplate 은 Mybatis Spring 연동 모듈의 핵심
     * 2. SqlSessionTemplate 은 SqlSession 을 구현하고, 코드에서 SqlSession 을 대체하는 역할을 한다
     * 3. SqlSessionTemplate 은 쓰레드에 안전하고 여러개의 DAO 나 Mapper 에서 공유할 수 있다
     * 4. 필요한 시점에 세션을 닫고, 커밋 또는 롤백하는 것을 포함한 세션의 생명주기를 관리
     */
    @Bean
    fun sqlSession(): SqlSessionTemplate = SqlSessionTemplate(sqlSessionFactory())

}