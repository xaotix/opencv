# opencv
Utilizando a biblioteca em python

<h2><b>Criar Rede</h2><b>


<b>Detecção Manual:</b>

Você vai precisar detectar manualmente a área em que se encontra o objeto que deseja detectar imagem por imagem. 
Para facilitar este trabalho, reúna todas as imagens em um diretório específico e utilize o comando opencv_annotation.

<b> Criando as Amostras: </b>
Após ter detectado manualmente, o opencv_annotation grava as informações em um documento chamado “ -info “ por padrão.
Este documento agora será usado para criar as amostras propriamente ditas.

<b> Treinando a Rede: </b>
Para treinar a rede você utilizará o comando opencv_traincascade. Note que este processo irá analisar imagem por imagem e pode demorar um bom tempo. 
Tudo depende de quantas imagens você possui em seu set de amostras.
Após finalizado o processo, será gerado um arquivo .xml, o qual você utilizará para rodar seu algoritmo que detectará o objeto que você treinou pra detectar.

<h3><b> Detectar Mão </h3></b>

[![Detectar Mão](http://img.youtube.com/vi/ke1l9JEd-aU/0.jpg)](https://www.youtube.com/watch?v=ke1l9JEd-aU "Detectar Mão")


<h3><b> Detectar Pessoas: </h3></b>

[![Detectar Pessoas](http://img.youtube.com/vi/pNB2UzUjLAE/0.jpg)](https://www.youtube.com/watch?v=pNB2UzUjLAE "Detectar Pessoas")

<h3><b> Detectar Siamês</h3></b>
<p>Codamos um detector de gatos siameses
<p>O detector localiza o rosto da gata e indica o nome da mesma.

[![Detectar Siamês](http://img.youtube.com/vi/6tms21_Qq7c/0.jpg)](https://www.youtube.com/watch?v=6tms21_Qq7c "Detectar Siamês")
