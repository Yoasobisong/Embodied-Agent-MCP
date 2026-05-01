/**
 * File: stm32_firmware/main.c
 * Target: STM32G431KBT6
 * Note: ADC VDDA Pin is P15 (Pin 15 on the package)
 */

#include "stm32g4xx_hal.h"
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

#define DOF_COUNT 26
#define UART_RX_BUFFER_SIZE 128

UART_HandleTypeDef huart1;
TIM_HandleTypeDef htim2;
TIM_HandleTypeDef htim3;
TIM_HandleTypeDef htim4;
// 假设使用了多个定时器通道来凑齐26路PWM...

uint8_t rx_buffer[UART_RX_BUFFER_SIZE];
uint8_t rx_data;
uint16_t rx_index = 0;

// 26个自由度的当前目标PWM占空比
uint16_t target_pwm[DOF_COUNT] = {0};

void SystemClock_Config(void);
static void MX_GPIO_Init(void);
static void MX_USART1_UART_Init(void);
static void MX_TIM_PWM_Init(void);

// 简易 JSON/指令解析：假设格式为 {"exp": ID} 或 E:ID\n
void ExecuteExpression(int expression_id) {
    // 根据表情 ID 查表设定 26 自由度舵机 PWM 占空比
    // 伪代码示例：
    for(int i=0; i<DOF_COUNT; i++) {
        target_pwm[i] = 1500 + (expression_id * 10) + (i * 5); // 1500us 为中位
        // 实际应用中会调用 __HAL_TIM_SET_COMPARE(&htimX, TIM_CHANNEL_Y, target_pwm[i]);
    }
    printf("Executed expression: %d\r\n", expression_id);
}

// 串口接收中断回调
void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart) {
    if (huart->Instance == USART1) {
        if (rx_data == '\n') {
            rx_buffer[rx_index] = '\0';
            
            // 简易解析逻辑：寻找 "exp" 字段
            char *ptr = strstr((char*)rx_buffer, "\"exp\":");
            if (ptr != NULL) {
                int exp_id = atoi(ptr + 6);
                ExecuteExpression(exp_id);
            }
            rx_index = 0;
            memset(rx_buffer, 0, UART_RX_BUFFER_SIZE);
        } else {
            if (rx_index < UART_RX_BUFFER_SIZE - 1) {
                rx_buffer[rx_index++] = rx_data;
            }
        }
        HAL_UART_Receive_IT(&huart1, &rx_data, 1);
    }
}

int main(void) {
    HAL_Init();
    SystemClock_Config();
    MX_GPIO_Init();
    MX_USART1_UART_Init();
    MX_TIM_PWM_Init();

    // 开启串口接收中断
    HAL_UART_Receive_IT(&huart1, &rx_data, 1);

    while (1) {
        // 主循环可处理平滑插值逻辑，逐步调整当前PWM逼近target_pwm
        HAL_Delay(10); 
    }
}

// 此处省略由 STM32CubeMX 生成的标准 Init 函数实现...
static void MX_GPIO_Init(void) { /* ADC VDDA P15 configured via hardware layout */ }
static void MX_USART1_UART_Init(void) { /* ... */ }
static void MX_TIM_PWM_Init(void) { /* ... */ }
