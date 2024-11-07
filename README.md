# Pratica-em-Pesquisa

script-NPB.sh

- O script executa todos os testes do NPB e salva os resultados de "Time in seconds" no arquivo "benchmark_times.txt"

benchmark_times.txt

- É o resultado de script-NPB.SH

calculoMedia.py

- Pega o resultado do script-NPB no arquivo benchmark_times.txt e faz as médias de todas as plataformas para cada número de threads.

medidas_timeInSeconds.txt

- É a saída do programa calculoMedia.py so que em um .txt

graficosNPB.py

- É o codigo que gera os gráficos baseado no medidas_timeInSeconds.txt, porém todos os resultados foram passados a mão.




# INSTALAÇÕES

- Python

      sudo apt install python3


Bixar matplotlib:

  - Baixar pelo pip:

        pip3 install matplotlib 

  - Baixar pelo gerenciador de pacotes debian:

        sudo apt install python3-matplotlib


Compilar:

        python3 <nome_do_arquivo>.py


# METODOLOGIA 2 

 com os testes rodados pegando a energia com o monitor.sh, foi gerado um output com as metricas de energia e pa.
 ai com todos os benchs do NPB foram rodados enquanto a energia era pega. 
 o generate_csv.sh vai ir na pasta TESTES-NPB e gerar um csv com o nome da aplicação, o numero de threads e o elapsed_time, porem o date que precisa para passar pelo parser nao esta nesse csv.

entoa agora precisa reacionar os date que estao na pasta DATE junto com as outras informações. FÉ!
