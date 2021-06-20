package com.lostark.lohyup

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication

@SpringBootApplication(proxyBeanMethods = false)
class LohyupApplication

fun main(args: Array<String>) {
    runApplication<LohyupApplication>(*args)
}
