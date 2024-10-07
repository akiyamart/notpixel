import asyncio
from contextlib import suppress
# import psutil

from utils.launcher import process

# # Константы
# SECOND = 1
# MINUTE = 60
# MONTH = 30 * 24 * 60 * 60  # 30 дней в секундах

# # Описание класса для отслеживания трафика
# class TrafficMonitor:
#     def __init__(self):
#         self.previous_bytes_sent = 0
#         self.previous_bytes_recv = 0

#     def get_traffic(self):
#         # Получаем статистику сети
#         net_io = psutil.net_io_counters()
#         return net_io.bytes_sent, net_io.bytes_recv

#     async def calculate_traffic_last_minute(self):
#         # Сохраняем начальные значения
#         self.previous_bytes_sent, self.previous_bytes_recv = self.get_traffic()
        
#         # Ждем минуту
#         await asyncio.sleep(MINUTE)

#         # Получаем конечные значения
#         bytes_sent_end, bytes_recv_end = self.get_traffic()

#         # Вычисляем трафик за минуту
#         sent_last_minute = bytes_sent_end - self.previous_bytes_sent
#         recv_last_minute = bytes_recv_end - self.previous_bytes_recv
        
#         return sent_last_minute + recv_last_minute

#     def estimate_monthly_traffic(self, last_minute_traffic):
#         estimated_monthly_traffic = last_minute_traffic * (MONTH / MINUTE)
#         return estimated_monthly_traffic


# async def monitor_traffic(traffic_monitor):
#     while True:
#         last_minute_traffic = await traffic_monitor.calculate_traffic_last_minute()
#         monthly_estimated_traffic = traffic_monitor.estimate_monthly_traffic(last_minute_traffic)

#         print(f"Трафик за последнюю минуту: {last_minute_traffic} байт")
#         print(f"Прогнозируемый трафик за месяц: {monthly_estimated_traffic} байт")

#         await asyncio.sleep(SECOND)  # Задержка перед следующим циклом


# async def main():
#     traffic_monitor = TrafficMonitor()

#     # Запускаем мониторинг трафика параллельно с другими задачами
#     await asyncio.gather(
#         monitor_traffic(traffic_monitor),
#         process()  # Ваша оригинальная асинхронная функция process
#     )

if __name__ == '__main__':
    with suppress(KeyboardInterrupt):
        asyncio.run(process())
