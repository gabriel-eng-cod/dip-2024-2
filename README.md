# Image Generator from Normal Distribution

Este repositório contém um script em Python para gerar imagens em tons de cinza, cujos valores de pixels são amostrados de uma distribuição normal.

## 📌 Funcionalidades
- Gera uma imagem baseada em um **número de matrícula** (usado como semente aleatória);
- Define dimensões personalizadas (**largura e altura**);
- Controla os parâmetros da distribuição normal (**média e desvio padrão**);
- Salva a imagem gerada no caminho especificado.

## 🛠️ Tecnologias Utilizadas
- Python
- OpenCV
- NumPy
- argparse

## 🚀 Como Usar

**Execute o script**:
```sh
python script.py --registration_number 123456 --width 256 --height 256 --mean 128 --std 30 --output output.png
```

🔹 **Parâmetros**:
- `--registration_number`: Número de matrícula do aluno (usado como semente aleatória)
- `--width`: Largura da imagem gerada
- `--height`: Altura da imagem gerada
- `--mean`: Média da distribuição normal
- `--std`: Desvio padrão da distribuição normal
- `--output`: Caminho para salvar a imagem gerada

