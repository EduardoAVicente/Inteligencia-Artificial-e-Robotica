## <a name="_5nl6pkcag3dw"></a>Integrantes:

Eduardo Antunes Vicente RA: 22.121.010-7

Ana Jéssica Soares da Silva RA: 22.121.100-6

Neste laboratório foram usados como base de dados os arquivos bank.arff, CriterioMedia.arff, CriterioProvas.arff, nas quais foram expostas a um algoritmo de aprendizado indutivo. Foi realizado o cálculo da entropia das árvores geradas, sendo seu cálculo uma ótima ferramenta para determinar o nível de impureza de um nó, tendo seu valor variando de 0 a 1, sendo quanto mais próximo de 1 maior seu nível de entropia.
## <a name="_o8ifoxxn4bli"></a>Principais dificuldade

Durante esta experiência a principal dificuldade foi realizar a codificação das string das variáveis não alvo de forma a não comprometer o funcionamento do código.

## <a name="_diipevsthaaz"></a>árvores e Matrizes de confusão encontradas

**Base de dados: CriterioProvas.arff**

entropia(73,-234)=-(73/307)log2(73/307)-(73/307)log2(234/307)=0.791

![](images/Aspose.Words.07d3d54e-8b2c-4250-91be-7d08df7f79c1.001.png)

![](images/Aspose.Words.07d3d54e-8b2c-4250-91be-7d08df7f79c1.002.png)

**Base de dados: CriterioMedia.arff**

entropia(43,-161)=-(43/204)log2(43/204)-(43/204)log2(161/204)=0.545

![](images/Aspose.Words.07d3d54e-8b2c-4250-91be-7d08df7f79c1.003.png)

![](images/Aspose.Words.07d3d54e-8b2c-4250-91be-7d08df7f79c1.004.png)

**Base de dados: bank.arff**

entropia(521,-4000)=-(521/4540)log2(521/4540)-(521/4540)log2(4000/4540)=0.379
![](images/Aspose.Words.07d3d54e-8b2c-4250-91be-7d08df7f79c1.005.png)![ref1]<a name="_ackbaa90zb3j"></a>
Comparação entre algoritmos
-------------------------------------------------------------------------------------------------

Para uma análise aprimorada, foram empregados dois algoritmos distintos na avaliação da base de dados bank: os algoritmos A e B. Como demonstrado nos resultados apresentados abaixo, embora ambos tenham o mesmo objetivo e utilizem a mesma base de dados, geraram resultados divergentes. Essa disparidade pode ser atribuída principalmente às diferentes formas de codificação de strings pelos algoritmos, além do fato de que o algoritmo A treina os dados como um todo, sem qualquer tipo de divisão, enquanto o algoritmo B os divide em conjuntos de treinamento.

**Algoritmo A:**

![](images/Aspose.Words.07d3d54e-8b2c-4250-91be-7d08df7f79c1.007.png)

![ref2]













**Algoritmo B:**

![](images/Aspose.Words.07d3d54e-8b2c-4250-91be-7d08df7f79c1.009.png)	![](images/Aspose.Words.07d3d54e-8b2c-4250-91be-7d08df7f79c1.010.png)

[ref1]: images/Aspose.Words.07d3d54e-8b2c-4250-91be-7d08df7f79c1.006.png
[ref2]: images/Aspose.Words.07d3d54e-8b2c-4250-91be-7d08df7f79c1.008.png
