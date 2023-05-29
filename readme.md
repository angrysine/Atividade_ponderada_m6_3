# Atividade ponderada 3 módulo 6

## Introdução

Esse repositório contem 4 arquivos e 1 pasta:

1. crack_detection.py : testa o modelo desenvolvido com as imagens da pasta test_images
2. model.pt: o modelo desenvolvido
3. read.md: o read me do projeto
4. video: video demonstrando o projeto

## Link do colab

O modelo foi treinado em um colab cujo link é : <https://colab.research.google.com/drive/1pCvgNnz6tZZtPtZjL2F1IfisjwWXRt5f?usp=sharing>
nesse notebook treinamos o modelo do yolo de instance segmentation usando o dataset do roboflow. Nenhuma máscara foi aplicada nas imagens já que a máscara testei que tornava as imagens preto e branco não obteve resultados ao modelo com dataset normal.

## testando o modelo

Ao rodar o arquivo crack_detection.py todas as imagens na pasta test_images são verificadas pelo modelo e após isso as imagens de resultado aparecem na tela 1 por 1, quando o usário aperta "a" é abortado o processo e se ele aperatar qualquer outra tecla a próxima imagem é mostrada.

## Vídeo demonstração

O video se encontra no diretório e tem nome video.mp4


