# **Aula 03: Sistema estrutural, pré-dimensionamento e lançamento estrutural**

```{admonition} Onde estamos?
:class: destaque-azul

O curso está organizado em torno das seguintes etapas de projeto:

1. Conceitos gerais sobre o projeto de pontes
2. Ações na superestrutura
3. Análise computacional com carga móvel
4. Dimensionamento da longarina
5. Dimensionamento do tabuleiro
6. Dimensionamento da transversina
7. Dimensionamento da mesoestrutura
8. Aparelhos de apoio

Esta aula trata do pré-dimensionamento do sistema estrutural e do lançamento estrutural — a base geométrica sobre a qual as ações e os dimensionamentos das próximas aulas serão construídos.
```

## 1. Sistema estrutural e seu pré-dimensionamento

Segundo O'Connor [[1]](#ref-1), a seleção do material e do esquema estrutural é uma tarefa complexa, que só pode ser determinada considerando-se todos os fatores que afetam o projeto de cada sistema estrutural em particular. Para isso, o autor apresenta a Figura 1.1 com diversas estruturas em função do seu material e da tipologia do sistema, com destaque para o vão máximo em serviço utilizado em cada um deles.

**Figura 1.1 — Comprimento de vão para vários tipos de superestruturas.** Fonte: O'Connor [[1]](#ref-1).

| Tipo estrutural | Material | Faixa de vãos (m) | Vão máximo em serviço (m) |
|---|---|---|---|
| Laje | Concreto | 0 – 12,2 | — |
| Viga | Concreto | 12,2 – 213,4 | 207,8 (Bendorf) |
| Viga | Metálica | 30,4 – 262,1 | 260,9 (Sava I) |
| Viga atirantada | Concreto | ≤ 243,8 | 235,0 (Maracaibo) |
| Viga atirantada | Metálica | 91,4 – 335,3 | 320,0 (Knie) |
| Treliça | Metálica | 91,4 – 548,6 | 548,6 (Quebec, ferroviária) / 480,3 (Greater New Orleans, rodoviária) |
| Arco | Concreto | 91,4 – 304,8 | 304,8 (Gladesville) |
| Arco | Treliça metálica | 243,8 – 518,2 | 510,5 (Bayonne) |
| Arco | Nervura metálica | 121,9 – 365,8 | 365,8 (Port Mann) |
| Pênsil | Metálica | 304,8 – 1371,6 | 1298,4 (Verrazano) |

De acordo com Areias Neto [[2]](#ref-2), para a fixação do comprimento da ponte deve-se levar em conta aspectos relacionados à seção de vazão necessária e ao projeto da estrada (perfil longitudinal). Araújo [[3]](#ref-3) afirma que o traçado de pontes em pequenos rios é definido pelo projetista da estrada durante a elaboração do traçado da via; quando, porém, a via cruza médios ou grandes rios, a posição da ponte pode determinar o traçado da via. Nesse caso, seguem alguns critérios para a posição da ponte:

a) transpor o canal principal ou vale no local mais estreito possível e mais próximo ao traçado original da via;
b) o canal principal deve ser transposto, de preferência, perpendicularmente à direção do escoamento do rio;
c) no caso de ponte esconsa, deve-se evitar eixos de pilares no meio do rio, onde a velocidade de escoamento d'água é maior, diminuindo a erosão localizada na base do pilar (Figura 1.2);
d) deve-se evitar transpor um rio logo após a região onde deságua um afluente (Figura 1.3) — a melhor posição para transposição é mais a jusante da região de deságue;
e) evitar transpor em locais onde possa haver, ao longo da vida útil da estrutura, mudanças na seção transversal do rio;
f) no cruzamento de rios de pequena vazão, é recomendável evitar curvas para a transposição.

```{figure} ../_static/aulas/lancamento-estrutural/fig-1-2.png
:alt: Erosão localizada na base de um pilar e contato com a água
:width: 90%
:align: center

**Figura 1.2** – Erosão localizada na base de um pilar (vista lateral) e vista superior de uma ponte esconsa. Fonte: Araújo [[3]](#ref-3).
```

```{figure} ../_static/aulas/lancamento-estrutural/fig-1-3.png
:alt: Transposição de rio com afluente
:width: 70%
:align: center

**Figura 1.3** – Transposição de rio com afluente. Fonte: Araújo [[3]](#ref-3).
```

Neste texto serão abordados os sistemas em concreto armado com solução de vigas de eixo reto, sendo necessárias algumas proposições de pré-dimensionamento do sistema estrutural para soluções em viga apoiada e viga contínua.

### 1.1 Algumas especificações para longarinas

Areias Neto [[2]](#ref-2) indica, para sistemas simplesmente apoiados, o seguinte:

$$
l \le 25\text{ m} \quad \text{(recomendação para pontes rodoviárias em concreto armado)}
$$

$$
h_{\text{long}} > \frac{l}{14} \quad \text{(Manual DNIT [[4]](#ref-4))}
\qquad\qquad
b_{w,\text{long}} \ge 25\text{ cm} \quad \text{(Manual DNIT [[4]](#ref-4))}
$$

No caso de soluções isostáticas com balanços (Figura 1.4), a recomendação de Areias Neto [[2]](#ref-2) — valor similar ao apresentado pelo DNIT [[4]](#ref-4) — é:

$$
\frac{l}{5} \le a \le \frac{l}{2}
$$

```{figure} ../_static/aulas/lancamento-estrutural/fig-1-4.png
:alt: Viga isostática com balanço
:width: 70%
:align: center

**Figura 1.4** – Viga isostática com balanço. Fonte: Areias Neto [[2]](#ref-2).
```

Araújo [[3]](#ref-3) replica algumas recomendações extras do DNIT [[4]](#ref-4) para o uso dos balanços:

- aterro com altura limitada a oito metros, ou menos;
- aterro de acesso executado antes da obra de arte;
- balanço ($a$) com comprimento máximo de $7{,}5\text{ m}$, com flecha inferior a $2\text{ cm}$;
- uso de laje de transição com comprimento mínimo de $4\text{ m}$.

Em sistema de viga contínua, Areias Neto [[2]](#ref-2) faz as seguintes recomendações:

**a) Vigas contínuas com dois vãos** (Figura 1.5): $l_1 = l_2$ e $a = l_1/4$.

```{figure} ../_static/aulas/lancamento-estrutural/fig-1-5.png
:alt: Viga contínua com dois vãos
:width: 80%
:align: center

**Figura 1.5** – Viga contínua com dois vãos. Fonte: Areias Neto [[2]](#ref-2).
```

**b) Vigas contínuas com três e quatro vãos internos** (Figura 1.6): $0{,}60\,l_2 \le l_1 \le 0{,}80\,l_2$ e $a = l_1/4$.

```{figure} ../_static/aulas/lancamento-estrutural/fig-1-6.png
:alt: Geometria da viga contínua com três e quatro vãos internos
:width: 90%
:align: center

**Figura 1.6** – Geometria da viga contínua: (a) situação para três vãos internos; (b) situação para quatro vãos internos. Fonte: Areias Neto [[2]](#ref-2).
```

### 1.2 Algumas especificações para tabuleiro e lajes em balanço

Quanto à seção transversal de lajes, o manual do DNIT [[4]](#ref-4) de obras de arte apresenta a Tabela 1.1.

**Tabela 1.1 — Espessura da laje.** Fonte: DNIT [[4]](#ref-4).

| Vão da laje (m) | Espessura da laje (cm) |
|---:|---:|
| 2 | 15 |
| 3 | 18 |
| 4 | 20 |
| 5 | 22 |
| 6 | 25 |

O DNIT [[4]](#ref-4) afirma que, em concreto armado convencional, as lajes são utilizadas para vãos até $15\text{ m}$, com relação altura/vão da ordem de $1/15$ em vãos isostáticos, e $1/20$ a $1/24$ em vãos contínuos.

A NBR 7187 [[5]](#ref-5) traz as seguintes exigências mínimas quanto às dimensões das lajes maciças:

a) lajes destinadas à passagem de tráfego ferroviário: $h \ge 20\text{ cm}$;
b) lajes destinadas à passagem de tráfego rodoviário: $h \ge 15\text{ cm}$;
c) demais casos: $h \ge 12\text{ cm}$.

### 1.3 O gabarito das pontes

De acordo com Pfeil [[6]](#ref-6), os **gabaritos** são os conjuntos de espaços livres que o projeto de uma ponte deve apresentar para atender à sua finalidade. De forma geral, podem-se especificar os gabaritos conforme a implantação da estrutura:

**a) Estruturas construídas sobre rodovias:** devem respeitar espaços livres necessários ao tráfego de caminhões, com altura livre de $5{,}50\text{ m}$ (Figura 1.7).

```{figure} ../_static/aulas/lancamento-estrutural/fig-1-7.png
:alt: Gabarito para obras de arte sobre rodovias
:width: 90%
:align: center

**Figura 1.7** – Gabarito para obras de arte sobre rodovias: (a) rodovia de pista simples; (b) rodovia de pista dupla. Fonte: Pfeil [[6]](#ref-6).
```

**b) Estruturas construídas sobre ferrovias:** devem respeitar espaços livres necessários ao tráfego de trens (Figura 1.8).

```{figure} ../_static/aulas/lancamento-estrutural/fig-1-8.png
:alt: Gabarito para obras de arte sobre ferrovias
:width: 90%
:align: center

**Figura 1.8** – Gabarito para obras de arte sobre ferrovias: (a) linha simples; (b) linha dupla. Fonte: Pfeil [[6]](#ref-6).
```

**c) Estruturas construídas sobre vias navegáveis:** para vias navegáveis a chatas e rebocadores, é comum prever altura livre de $3{,}50\text{ m}$ a $5{,}0\text{ m}$ acima do nível máximo de cheia, com largura mínima igual à largura máxima da embarcação mais $1\text{ m}$ (Figura 1.9). Para vias não navegáveis, normalmente se estabelece altura livre de $2\text{ m}$ acima do nível de máxima cheia.

```{figure} ../_static/aulas/lancamento-estrutural/fig-1-9.png
:alt: Exemplo de ponte com gabarito de navegação
:width: 100%
:align: center

**Figura 1.9** – Exemplo de ponte sobre o Rio Paraguai, em Cáceres (MT), com gabarito de navegação da ordem de $30\text{ m}$ de largura por $12\text{ m}$ de altura acima do nível máximo de cheia das águas. Fonte: Pfeil [[6]](#ref-6).
```

### 1.4 Algumas especificações para os pilares e aparelhos de apoio

O pré-dimensionamento dos pilares e dos aparelhos de apoio de uma ponte depende da previsão de cargas nessas estruturas. Feita essa previsão, as condições de pré-dimensionamento do pilar seguem as mesmas observações impostas aos elementos de estruturas prediais normalmente estudados nas disciplinas de concreto armado.

**a) Pré-dimensionamento dos pilares:**

$$
N_d^{*} = \alpha \cdot N_k^{*}
\qquad\qquad
A_c = \frac{1{,}50 \cdot N_d^{*}}{0{,}50 \cdot f_{ck} + 0{,}42} \ge 360\text{ cm}^2
$$

em que $\alpha = 1{,}8$ para pilares intermediários, $\alpha = 2{,}2$ para pilares de extremidade e $\alpha = 2{,}5$ para pilares de canto; $A_c$ é a área da seção de concreto do pilar (cm²); $N_d$, a força normal aproximada de cálculo (kN); e $f_{ck}$, a resistência característica de cálculo (kN/cm²).

```{admonition} Ordem de verificação
:class: destaque-vermelho

É recomendável que a verificação das dimensões dos pilares seja feita **após** a previsão das dimensões dos aparelhos de apoio, visto que estes devem se encaixar dentro dos pilares.
```

**b) Pré-dimensionamento dos aparelhos de apoio em Neoprene.** Utiliza-se a NBR 9062 [[7]](#ref-7), item 7.2.1.6 e Anexo A:

- Tensão limitante para aparelhos de apoio simples: $\sigma_k = \dfrac{N_k^{*}}{a \cdot b} \le 7\text{ MPa}$, em que $a$ (menor dimensão em planta) e $b$ designam as dimensões em planta do aparelho.
- Tensão limitante para aparelhos de apoio fretados:

| Dimensão $a$ | Tensão limite $\sigma_k$ |
|---|---|
| $a \le 15\text{ cm}$ | $\le 8\text{ MPa}$ |
| $15\text{ cm} < a \le 20\text{ cm}$ | $\le 11\text{ MPa}$ |
| $20\text{ cm} < a \le 30\text{ cm}$ | $\le 12{,}5\text{ MPa}$ |
| $a > 30\text{ cm}$ | $\le 15\text{ MPa}$ |

Quanto à altura, para uma verificação inicial adota-se o critério da NBR 9062 [[7]](#ref-7) que dispensa a verificação de estabilidade da almofada:

$$
h_{\text{almofada}} \le \frac{a}{5}
$$

## 2. Lançamento estrutural

Para o lançamento estrutural, o primeiro dado a que o engenheiro estrutural tem acesso é o levantamento topográfico (Figura 2.1), fornecido pela concessionária responsável pelo projeto. Após a visualização do estaqueamento e do eixo para colocação da ponte, é necessário realizar um estudo hidrológico para determinação da altura de máxima cheia.

```{figure} ../_static/aulas/lancamento-estrutural/fig-2-1.png
:alt: Croqui da trajetória do leito do rio e marcação do estaqueamento
:width: 70%
:align: center

**Figura 2.1** – Croqui da trajetória do leito do rio e marcação do estaqueamento.
```

A determinação da vazão de projeto e da cota de máxima cheia utiliza a fórmula de Manning:

$$
V = \frac{1}{n}\,R^{2/3}\,J^{1/2}
\qquad\qquad
Q = A \cdot V
$$

em que $Q$ é a vazão ($\text{m}^3/\text{s}$); $A$, a área da seção molhada ($\text{m}^2$); $K$, o coeficiente de rugosidade de Strickler; $n$, o coeficiente de rugosidade de Manning; $V$, a velocidade de escoamento ($\text{m/s}$); $R$, o raio hidráulico ($\text{m}$, dado por $R = A/P$, sendo $P$ o perímetro molhado); e $J$, a declividade do fundo ($\text{m/m}$).

Dados do projeto de Araújo [[3]](#ref-3): $Q = 691{,}02\text{ m}^3/\text{s}$; cota de fundo $= 208{,}678\text{ m}$.

**Tabela 2.1 — Determinação da vazão de projeto e cota referente à máxima cheia.** Fonte: Araújo [[3]](#ref-3).

| Cota (m) | Área (m²) | Perímetro (m) | $R_H$ (m) | $V$ (m/s) | $Q$ (m³/s) |
|---:|---:|---:|---:|---:|---:|
| 209,08 | 4,859 | 20,425 | 0,238 | 0,439 | 2,133 |
| 209,68 | 17,264 | 21,816 | 0,791 | 0,977 | 16,875 |
| 210,08 | 25,771 | 22,808 | 1,130 | 1,240 | 31,953 |
| 211,08 | 48,453 | 26,067 | 1,859 | 1,728 | 83,721 |
| 212,08 | 74,375 | 30,772 | 2,417 | 2,058 | 153,086 |
| 213,08 | 104,708 | 36,065 | 2,903 | 2,326 | 243,521 |
| 214,08 | 142,999 | 52,340 | 2,732 | 2,233 | 319,383 |
| 215,08 | 201,915 | 65,798 | 3,069 | 2,414 | 487,332 |
| 216,08 | 264,955 | 69,404 | 3,818 | 2,792 | 739,698 |

Com a cota de máxima cheia calculada (MCC) determinada, o lançamento estrutural define o posicionamento dos apoios, das cotas dos pilares e da altura livre até o tabuleiro (Figura 2.2).

```{figure} ../_static/aulas/lancamento-estrutural/fig-2-2.png
:alt: Elevação longitudinal com a marcação do estaqueamento e MCC
:width: 100%
:align: center

**Figura 2.2** – Elevação longitudinal com a marcação do estaqueamento e da MCC, incluindo as cotas dos pilares (P1 e P2), da máxima cheia calculada, da máxima cheia observada e do nível d'água atual.
```

## Referências

(ref-1)=
**[1]** O'CONNOR, C. *Pontes — Superestruturas*. vol. 1, 2 vols. LTC, 1976.

(ref-2)=
**[2]** AREIAS NETO, A. C. de. *Projeto e Cálculo de Pontes de Concreto Armado*. vol. 1. Rio de Janeiro: IME, 1977.

(ref-3)=
**[3]** ARAÚJO, D. de L. *Projeto de ponte em concreto armado com duas longarinas*. 2. ed. Goiânia: UFG, 2018.

(ref-4)=
**[4]** DEPARTAMENTO NACIONAL DE INFRAESTRUTURA DE TRANSPORTES (DNIT). *Manual de Projeto de Obras de Arte Especiais*. Brasília: Ministério da Infraestrutura, 1996.

(ref-5)=
**[5]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 7187**: *Projeto de pontes de concreto armado e de concreto protendido — Procedimento*. Rio de Janeiro: ABNT, 2003.

(ref-6)=
**[6]** PFEIL, W. *Pontes em Concreto Armado: elementos de Projeto, Solicitações e Superestrutura*. vol. 1, 2 vols. Rio de Janeiro: LTC, 1990.

(ref-7)=
**[7]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 9062**: *Projeto e execução de estruturas de concreto pré-moldado*. Rio de Janeiro: ABNT, 2017.
