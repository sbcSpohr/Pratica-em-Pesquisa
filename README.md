# Pratica-em-Pesquisa

scriptBenchmarks.sh 
  - Executa todos os benchmarks do NPB-CPP

scriptGrep.sh
  - Filtra apenas os 'time in seconds' dos resultados gerados pelo 'scriptBenchmarks'

media.py
  - Pega os dados filtrados pelo 'scriptGrep' e faz as medias

medias1.txt
 - Dados das medias feito pelo 'media.py'. Na parte do 'SER' embora esteja com threads de (1, 4, 8, 12)
  ele é feito apenas com 1 thread, então trocar o contexto de 'threads' para execuções.

graficos.py
  - Gera os gráficos a partir das medias calculadas
