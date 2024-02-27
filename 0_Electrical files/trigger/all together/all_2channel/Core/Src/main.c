#include "main.h"

uint8_t UART1_rxBuffer[2] = {0};
uint8_t UART1_tx_NA[16] = {"Not Acceptable!"};

uint8_t UART1_tx_ok[3] = {"OK"};

uint8_t data[2] = {'1','0'};

int wanted_freq = 19;
int wanted_comp = 49999;



char good_start = '0';


TIM_HandleTypeDef htim2;

UART_HandleTypeDef huart1;

void SystemClock_Config(void);
static void MX_GPIO_Init(void);
static void MX_USART1_UART_Init(void);
static void MX_TIM2_Init(void);



int main(void)
{

  HAL_Init();
  SystemClock_Config();
  MX_GPIO_Init();
  MX_USART1_UART_Init();
  MX_TIM2_Init();
	
		HAL_UART_Receive_IT( & huart1, UART1_rxBuffer, 1);

	
	
			wanted_comp=(500000 / wanted_freq)-1;
////////////frequency
		TIM2->ARR=wanted_comp;
/////////////duty cycle
		TIM2->CCR1 = (wanted_comp+1) * 0.01;
		TIM2->CCR2 = (wanted_comp+1) * 0.01;

	
	
	
//	__HAL_TIM_SET_COMPARE( & htim2, TIM_CHANNEL_1, 25000);
//	__HAL_TIM_SET_COMPARE( & htim2, TIM_CHANNEL_2, 25000);

	
  HAL_TIM_PWM_Start( & htim2, TIM_CHANNEL_1);
  HAL_TIM_PWM_Start( & htim2, TIM_CHANNEL_2);	
  while (1)
  {

		HAL_GPIO_TogglePin(led_GPIO_Port, led_Pin);
    HAL_Delay(50);
    //		
    //		//frequency
    //		TIM2->ARR=per;
    //		
    //		//duty cycle
    //		TIM2->CCR1 = (per+1) / 2;
    //		per -= 20;


		
  }

}

void HAL_UART_RxCpltCallback(UART_HandleTypeDef * huart) {
  ///////////////////////START COMMU/////////////////////////////////
  if (UART1_rxBuffer[0] == '%' && good_start == '0') {
    good_start = '1';
    HAL_UART_Receive_IT( & huart1, UART1_rxBuffer, 2);
    HAL_UART_Transmit( & huart1, UART1_rxBuffer, 1, 100);
  }

  /////////////////////// FREQ CHANGE //////////////////////////////
  else if (good_start == '1') {
		good_start = '0';
    data[0] = UART1_rxBuffer[0];
    data[1] = UART1_rxBuffer[1];
		if(data[0] >= 48 && data[0] <=57){
		wanted_freq=(data[0] - '0')*10 + (data[1]-'0');}
		
		wanted_comp=(500000 / wanted_freq)-1;
////////////frequency
		TIM2->ARR=wanted_comp;
/////////////duty cycle
		TIM2->CCR1 = (wanted_comp+1) * 0.01;
		TIM2->CCR2 = (wanted_comp+1) * 0.01;
		
    HAL_UART_Transmit( & huart1, UART1_tx_ok , 3, 100);
    HAL_UART_Receive_IT( & huart1, UART1_rxBuffer, 1);
//    good_start = '0';

  }
	
	
	
	else {
    HAL_UART_Transmit( & huart1, UART1_tx_NA, 16, 100);
    HAL_UART_Receive_IT( & huart1, UART1_rxBuffer, 1);
    good_start = '0';
  }

  //		TIM2->ARR=40000;

  //		else if(good_start=='0'){
  //    HAL_UART_Transmit(&huart1, UART1_tx_NA, 16, 100);

  //    HAL_UART_Receive_IT(&huart1, UART1_rxBuffer, 1);}

}

void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};


  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSE;
  RCC_OscInitStruct.HSEState = RCC_HSE_ON;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_NONE;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }

  /** Initializes the CPU, AHB and APB buses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_HSE;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV8;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV4;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_0) != HAL_OK)
  {
    Error_Handler();
  }

  /** Enables the Clock Security System
  */
  HAL_RCC_EnableCSS();
}

static void MX_TIM2_Init(void)
{

  /* USER CODE BEGIN TIM2_Init 0 */

  /* USER CODE END TIM2_Init 0 */

  TIM_MasterConfigTypeDef sMasterConfig = {0};
  TIM_OC_InitTypeDef sConfigOC = {0};

  /* USER CODE BEGIN TIM2_Init 1 */

  /* USER CODE END TIM2_Init 1 */
  htim2.Instance = TIM2;
  htim2.Init.Prescaler = 0;
  htim2.Init.CounterMode = TIM_COUNTERMODE_UP;
  htim2.Init.Period = 49999;
  htim2.Init.ClockDivision = TIM_CLOCKDIVISION_DIV1;
  htim2.Init.AutoReloadPreload = TIM_AUTORELOAD_PRELOAD_DISABLE;
  if (HAL_TIM_PWM_Init(&htim2) != HAL_OK)
  {
    Error_Handler();
  }
  sMasterConfig.MasterOutputTrigger = TIM_TRGO_RESET;
  sMasterConfig.MasterSlaveMode = TIM_MASTERSLAVEMODE_DISABLE;
  if (HAL_TIMEx_MasterConfigSynchronization(&htim2, &sMasterConfig) != HAL_OK)
  {
    Error_Handler();
  }
  sConfigOC.OCMode = TIM_OCMODE_PWM1;
  sConfigOC.Pulse = 0;
  sConfigOC.OCPolarity = TIM_OCPOLARITY_HIGH;
  sConfigOC.OCFastMode = TIM_OCFAST_DISABLE;
  if (HAL_TIM_PWM_ConfigChannel(&htim2, &sConfigOC, TIM_CHANNEL_1) != HAL_OK)
  {
    Error_Handler();
  }
  if (HAL_TIM_PWM_ConfigChannel(&htim2, &sConfigOC, TIM_CHANNEL_2) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN TIM2_Init 2 */

  /* USER CODE END TIM2_Init 2 */
  HAL_TIM_MspPostInit(&htim2);

}


static void MX_USART1_UART_Init(void)
{

  /* USER CODE BEGIN USART1_Init 0 */

  /* USER CODE END USART1_Init 0 */

  /* USER CODE BEGIN USART1_Init 1 */

  /* USER CODE END USART1_Init 1 */
  huart1.Instance = USART1;
  huart1.Init.BaudRate = 9600;
  huart1.Init.WordLength = UART_WORDLENGTH_8B;
  huart1.Init.StopBits = UART_STOPBITS_1;
  huart1.Init.Parity = UART_PARITY_NONE;
  huart1.Init.Mode = UART_MODE_TX_RX;
  huart1.Init.HwFlowCtl = UART_HWCONTROL_NONE;
  huart1.Init.OverSampling = UART_OVERSAMPLING_16;
  if (HAL_UART_Init(&huart1) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN USART1_Init 2 */

  /* USER CODE END USART1_Init 2 */

}

/**
  * @brief GPIO Initialization Function
  * @param None
  * @retval None
  */
static void MX_GPIO_Init(void)
{
  GPIO_InitTypeDef GPIO_InitStruct = {0};
/* USER CODE BEGIN MX_GPIO_Init_1 */
/* USER CODE END MX_GPIO_Init_1 */

  /* GPIO Ports Clock Enable */
  __HAL_RCC_GPIOC_CLK_ENABLE();
  __HAL_RCC_GPIOD_CLK_ENABLE();
  __HAL_RCC_GPIOA_CLK_ENABLE();
  __HAL_RCC_GPIOB_CLK_ENABLE();

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(led_GPIO_Port, led_Pin, GPIO_PIN_RESET);

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(GPIOA, pwm_out_1_Pin|pwm_out_2_Pin, GPIO_PIN_RESET);

  /*Configure GPIO pin : led_Pin */
  GPIO_InitStruct.Pin = led_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(led_GPIO_Port, &GPIO_InitStruct);

  /*Configure GPIO pins : up_btn_Pin dn_btn_Pin */
  GPIO_InitStruct.Pin = up_btn_Pin|dn_btn_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_IT_RISING;
  GPIO_InitStruct.Pull = GPIO_PULLDOWN;
  HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);

  /*Configure GPIO pins : pwm_out_1_Pin pwm_out_2_Pin */
  GPIO_InitStruct.Pin = pwm_out_1_Pin|pwm_out_2_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_PULLDOWN;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);

/* USER CODE BEGIN MX_GPIO_Init_2 */
/* USER CODE END MX_GPIO_Init_2 */
}

/* USER CODE BEGIN 4 */

/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */
  __disable_irq();
  while (1)
  {
  }
  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */
