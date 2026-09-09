# **Aula 04: Superestrutura de Pontes de Concreto — Ações, Trem-Tipo e Exemplo Numérico**

```{note}
Esta aula reúne o material de carregamentos fornecido para a disciplina: ações permanentes, trem-tipo rodoviário, distribuição transversal e exemplo da Ponte sobre o Rio Pau Seco.
```

```{warning}
Material em preparação. Algumas equações e etapas de cálculo não vieram no texto de origem, especialmente nas seções 3.2, 4.2 e 5.2 a 5.4. Os resultados numéricos abaixo foram transcritos do material fornecido e ainda precisam de conferência antes de serem usados no trabalho prático.

A revisão deve esclarecer a reserva de recapeamento (incluída nos 8 cm neste exemplo, mas separada nas diretrizes da aula de introdução), a posição das rodas e os limites da área carregada, a aplicação do CIA e a distinção entre cargas com efeitos dinâmicos e ações de cálculo nas combinações de estados limites.
```


Este documento compõe o material didático completo para o projeto e análise de superestruturas de pontes rodoviárias de concreto armado e protendido. Nele são abordadas a classificação das ações, o cálculo e distribuição do peso próprio, os veículos-tipo normativos, os coeficientes dinâmicos, a distribuição transversal por Linhas de Influência e um exemplo prático totalmente resolvido.


## 1. Classificação Geral das Ações e Base Normativa

As ações atuantes nas pontes são classificadas de acordo com sua permanência, variabilidade e natureza de aplicação. A estimativa e a combinação dessas ações seguem rigorosamente as prescrições das normas técnicas brasileiras:
 * NBR 6118 [[1]](#ref-1): Projeto de estruturas de concreto - Procedimento.
 * NBR 7187 [[2]](#ref-2): Projeto de pontes de concreto armado e de concreto protendido - Procedimento.
 * NBR 7188 [[3]](#ref-3): Carga móvel rodoviária e de pedestres em pontes, viadutos, passarelas e outras estruturas.
 * NBR 6120 [[4]](#ref-4): Cargas para o cálculo de estruturas de edificações.
 * Manual DNIT 698/1996 [[5]](#ref-5): Manual de Projetos de Obras d'Arte Especiais.

### Classificação das Ações na Superestrutura


 * Ações Permanentes Diretas e Indiretas:
   * Peso próprio dos elementos estruturais (vigas longarinas, lajes, mísulas, transversinas).
   * Peso próprio da pavimentação asfáltica e camada de recapeamento futuro.
   * Elementos de proteção (barreiras New Jersey, guarda-corpos e plintos).
   * Empuxos de terra e água, e efeitos diferidos no tempo (retração e fluência do concreto).
 * Ações Variáveis Diretas e Indiretas:
   * Cargas móveis (veículos rodoviários, tráfego de pedestres e multidão).
   * Cargas de construção, ação do vento e variações térmicas (uniforme e gradiente).
   * Empuxo de terra provocado por cargas móveis e força da correnteza d'água.
 * Ações Dinâmicas e Excepcionais:
   * Efeitos dinâmicos do tráfego (impacto vertical e adicional).
   * Forças de frenagem, aceleração e força centrífuga em curvas.
   * Colisões de veículos ou embarcações contra a estrutura.

## 2. Parâmetros e Determinação das Ações Permanentes

### 2.1 Pesos Específicos Mínimos e Especificações Normativas
Conforme a NBR 7187 [[2]](#ref-2) e a NBR 6120 [[4]](#ref-4), devem ser adotados os seguintes valores mínimos para os materiais constitutivos:
| Elemento / Material | Valor Adotado | Norma de Referência |
|---|---|---|
| Concreto Simples | $24\text{ kN/m}^3$ | NBR 7187 [[2]](#ref-2) (Item 7.1.1) |
| Concreto Armado ou Protendido | $25\text{ kN/m}^3$ | NBR 7187 [[2]](#ref-2) (Item 7.1.1) |
| Pavimentação Asfáltica (CBUQ) | $24\text{ kN/m}^3$ | NBR 7187 [[2]](#ref-2) (Item 7.1.2) |
| Adicional de Recapeamento | $2\text{ kN/m}^2$ no tabuleiro | NBR 7187 [[2]](#ref-2) (Item 7.1.2) |
| Solo Úmido (Aterro / Ala) | $18\text{ kN/m}^3$ (\phi \le 30^\circ) | NBR 7187 [[2]](#ref-2) (Item 7.1.4) |
| Guarda-Corpo (Pedestres) | $0{,}8\text{ kN/m}$ (H) / $2{,}0\text{ kN/m}$ (V) | NBR 6120 [[4]](#ref-4) / DNIT 698 [[5]](#ref-5) |
| Guarda-Corpo (Passeio Misto) | $1{,}5\text{ kN/m}$ (H) | NBR 6120 [[4]](#ref-4) |
Em projetos estruturais de pontes, a variação total das cargas permanentes entre a fase de pré-dimensionamento e o projeto executivo final não deve ser superior a *5%*.


### 2.2 Distribuição do Peso Próprio na Longarina

Para pontes com duas longarinas principais, o cálculo das cargas distribuídas ao longo do vão considera a metade da seção transversal em virtude da simetria geométrica.

```text
                [Barreira / Guarda-Corpo]
                          |
     =====================+===================== (Tabuleiro / Pavimento)
       \   Laje Balanço   |   Laje Central   /
        \                 |                 /
         +-----+   [Viga Longarina]   +----+
               |                      |
```



#### Componentes da Seção Transversal Corrente (Meio do Vão)


 * Viga Longarina: Alma de concreto retangular e variação de altura ao longo do vão.
 * Tabuleiro: Laje central e laje em balanço lateral.
 * Mísulas: Variações graduais de espessura na transição entre laje e viga.
 * Elementos de Proteção:
   * Barreira New Jersey: Concreto armado padronizado conforme o manual DNIT 698 [[5]](#ref-5) (seção transversal com área típica de $0{,}23\text{ m}^2$).
   * Guarda-Corpo Metálico: Considera-se uma base de concreto de $15\text{ cm} \times 10\text{ cm}$ somada ao peso próprio do perfil metálico e às sobrecargas da NBR 6120 [[4]](#ref-4).
 * Pavimentação: Camada de concreto betuminoso usinado a quente (CBUQ) com espessura média acrescida da reserva para recapeamento futuro.

#### Componentes das Regiões de Apoio e Extremidades


 * Alargamentos de Apoio: Engrossamentos da alma da viga longarina à medida que se aproxima dos apoios. Podem ser calculados como uma carga triangular distribuída ao longo da transição ou por meio da força resultante posicionada no centroide da geometria.
 * Transversinas: Vigas transversais de travamento e rigidez no apoio e ao longo do vão.
 * Vigas de Fechamento (Cortina) e Alas: Avaliadas como cargas pontuais aplicadas na extremidade em balanço do sistema estrutural. Deve-se contabilizar o peso do solo úmido retido sobre a cortina e a continuidade das barreiras e guarda-corpos.

## 3. Ações Variáveis e Carga Móvel (Trem-Tipo Rodoviário)

### 3.1 Veículos-Tipo Padrão (NBR 7188 [[3]](#ref-3))
A carga móvel simulada nas pontes rodoviárias combina um veículo pesado concentrado com uma carga distribuída de multidão.

#### Veículo-Tipo TB-450 (Rodovias de Tráfego Geral)


 * Peso Total: $450\text{ kN}$ (45 toneladas).
 * Eixos de Carga: 3 eixos verticais de $150\text{ kN}$ ($75\text{ kN}$ por roda).
 * Geometria em Planta:
   * Largura total do veículo: $3{,}00\text{ m}$.
   * Comprimento total do veículo: $6{,}00\text{ m}$.
   * Distância entre eixos: $1{,}50\text{ m}$.
   * Distância transversal entre rodas de um mesmo eixo: $2{,}00\text{ m}$.
   * Área de contato de cada roda: $0{,}20\text{ m} \times 0{,}50\text{ m}$.
 * Carga de Multidão (q): $5{,}0\text{ kN/m}^2$ aplicada uniformemente em toda a área de pista utilizável ao redor do veículo.

Conforme o item 5.1.1 da NBR 7188 [[3]](#ref-3), a carga de multidão $q$ é aplicada em toda a área do tabuleiro não ocupada pelo veículo-tipo, inclusive nas faixas que o margeiam longitudinal e transversalmente. A Figura 3.1 apresenta a planta com o posicionamento das rodas e os cortes esquemáticos (Seção A-A e Seção B-B) com a distribuição da carga de multidão $p$ e das cargas de eixo $P$.

```{figure} ../_static/aulas/carregamentos/esquema-tb-450.png
:alt: Esquema de cargas do veículo-tipo TB-450
:width: 90%
:align: center

**Figura 3.1** – Esquema de cargas do veículo-tipo TB-450: planta com o posicionamento das rodas e cortes esquemáticos (Seção A-A e Seção B-B) com a distribuição da carga de multidão $p$ e das cargas de eixo $P$. Fonte: NBR 7188 [[3]](#ref-3), item 5.1.1.
```


#### Veículo-Tipo TB-240 (Estradas Vicinais)


 * Peso Total: $240\text{ kN}$ (24 toneladas).
 * Eixos de Carga: 3 eixos verticais de $80\text{ kN}$ ($40\text{ kN}$ por roda).
 * Carga de Multidão (q): $4{,}0\text{ kN/m}^2$.

#### Passeios e Pedestres


 * Passeios Integrados: Carga uniformemente distribuída de $3{,}0\text{ kN/m}^2$ aplicada concomitante com a carga rodoviária na posição mais desfavorável.
 * Dimensionamento Local do Passeio: Carga móvel individual de $5{,}0\text{ kN/m}^2$.

### 3.2 Coeficientes de Majoração Dinâmica

Para simular o caráter dinâmico, imperfeições e a estocasticidade do tráfego, as cargas estáticas normativas são majoradas por três coeficientes principais:

#### 1. Coeficiente de Impacto Vertical (CIV)

Simula os efeitos dinâmicos causados pela passagem dos veículos. Conforme o item 5.1.3.1 da NBR 7188 [[3]](#ref-3), o CIV é determinado em função do vão teórico de referência $L_{iv}$:

$$
CIV = 1{,}35 \text{, para estruturas com vão inferior a } 10{,}0\text{ m}
$$

$$
CIV = 1 + 1{,}06 \cdot \left(\frac{20}{L_{iv} + 50}\right) \text{, para estruturas com vão entre } 10{,}0\text{ m e } 200{,}0\text{ m}
$$

Para vigas isostáticas, $L_{iv}$ é o próprio vão teórico do trecho. Em estruturas com balanço, adota-se o vão da peça. Em vigas contínuas, $L_{iv}$ corresponde à média aritmética dos vãos da estrutura.


#### 2. Coeficiente de Número de Faixas (CNF)

Conforme o item 5.1.3.2 da NBR 7188 [[3]](#ref-3), o CNF pondera a probabilidade da carga móvel ocorrer concomitantemente em $n$ faixas carregadas de uma determinada hipótese de carga, sendo dado por:

$$
CNF = 1 - 0{,}05 \cdot (n - 2) \text{, com } 1{,}0 \ge CNF \ge 0{,}9
$$

Quando não for determinada a largura correspondente à hipótese de carga, deve-se considerar $CNF = 1{,}0$.

Este coeficiente não se aplica ao dimensionamento de elementos estruturais transversais ao sentido do tráfego, como, por exemplo, lajes e transversinas.

#### 3. Coeficiente de Impacto Adicional (CIA)

Majora os esforços em virtude de irregularidades ou descontinuidades no pavimento:
 * Obras em Concreto Armado, Protendido ou Mistas: $CIA = 1{,}25$.
 * Obras em Aço: $CIA = 1{,}15$.

#### Expressões Finais Majoradas

A carga concentrada $Q$ e a carga distribuída $q$, aplicadas no nível do pavimento, devem ser determinadas por:

$$
Q = P \cdot CIV \cdot CNF \cdot CIA
$$

$$
q = p \cdot CIV \cdot CNF \cdot CIA
$$


## 4. Distribuição Transversal e Trem-Tipo na Longarina

### 4.1 Linhas de Influência (LI)
A Linha de Influência (LI) descreve a variação de um determinado efeito estrutural (reação de apoio, esforço cortante ou momento fletor) em uma seção fixa S, produzida pelo deslocamento de uma carga vertical unitária P=1 ao longo do tabuleiro da ponte.
  Carga Móvel P=1

```text
       |
```

  -----+---------------------------------------+----- (Superestrutura)

```text
       | x                                     |
```

    +-----+                                 +-----+
    | A   |                                 | B   |
    +-----+                                 +-----+


### 4.2 Metodologia para Posicionamento e Obtenção dos Esforços

 * Posicionamento Transversal Crítico:
   * O veículo-tipo deve ser posicionado na situação mais desfavorável no tabuleiro, encostado na barreira ou guarda-rodas lateral, maximizando o efeito na longarina de interesse.
   * O lado oposto do tabuleiro pode ficar descarregado para evitar o alívio de tensões, garantindo a envoltória máxima de projeto.
 * Avaliação por Reação de Apoio Transversal:
   * Utiliza-se o modelo simplificado de viga transversal (ou alavanca/grelha) para calcular a reação transferida à longarina por meio da linha de influência da reação de apoio \eta(x).
 * Cálculo da Carga Concentrada Equivalente na Longarina:
   
   
   (onde \eta_i é a ordenada da LI no ponto de aplicação de cada roda i).
 * Cálculo da Carga Distribuída Equivalente na Longarina:
   
   
   (onde \Omega representa as regiões transversais do tabuleiro carregadas pela multidão).
 * Aplicação dos Coeficientes Dinâmicos:
   * Multiplicam-se os valores P_{\text{longarina}} e q_{\text{longarina}} pelos coeficientes (CIV \cdot CNF \cdot CIA) para a obtenção das ações de cálculo finais.

## 5. Exemplo Prático Completo Resolvido: Ponte sobre o Rio Pau Seco

Apresenta-se a determinação completa das ações permanentes e variáveis para a Ponte sobre o Rio Pau Seco.

### 5.1 Dados Geométricos e Parâmetros de Projeto

 * Vão Teórico da Ponte (L): $25{,}00\text{ m}$ (Viga biapoiada isostática).
 * Largura Total do Tabuleiro (B): $9{,}00\text{ m}$.
 * Largura da Pista de Rolamento: $8{,}20\text{ m}$.
 * Número de Longarinas: 2 longarinas longitudinais de concreto armado.
 * Espaçamento entre Eixos das Longarinas (d): $5{,}00\text{ m}$.
 * Balanços da Laje do Tabuleiro (b_{\text{bal}}): $2{,}00\text{ m}$ para cada lado.
 * Número de Faixas do TB-450 (n): 2 faixas de $3{,}00\text{ m}$.
 * Área da Seção Transversal de Concreto no Meio do Vão (A_{\text{meio}}): $3{,}495\text{ m}^2$.
 * Área da Barreira New Jersey: $0{,}23\text{ m}^2$ por bordo.
 * Espessura Média do Pavimento Asfáltico (h_{\text{asf}}): $0{,}08\text{ m}$ ($8\text{ cm}$, incluindo recapeamento).

### 5.2 Cálculo da Carga Permanente Distribuída (g_{\text{long}})

Em virtude da simetria transversal, calcula-se a carga permanente atuante em uma longarina considerando metade da seção total:
 * Peso Próprio da Estrutura de Concreto:

*Equação ou desenvolvimento ausente no texto recebido; a completar.*

 * Peso Próprio da Barreira New Jersey:

*Equação ou desenvolvimento ausente no texto recebido; a completar.*

 * Peso Próprio da Pavimentação Asfáltica (CBUQ + Recapeamento):
   Com largura de pista atribuída de $4{,}10\text{ m}$ ($8{,}20\text{ m} / 2$):

*Equação ou desenvolvimento ausente no texto recebido; a completar.*

 * Carga Permanente Total Distribuída por Longarina (g_{\text{meio}}):

*Equação ou desenvolvimento ausente no texto recebido; a completar.*


### 5.3 Determinando os Coeficientes de Majoração Dinâmica

 * Coeficiente de Impacto Vertical (CIV):
   Com $L_{iv} = 25{,}00\text{ m}$:

*Equação ou desenvolvimento ausente no texto recebido; a completar.*

 * Coeficiente de Número de Faixas (CNF):
   Com n = 2 faixas de rolamento:

*Equação ou desenvolvimento ausente no texto recebido; a completar.*

 * Coeficiente de Impacto Adicional (CIA):
   Para estrutura de concreto armado:

*Equação ou desenvolvimento ausente no texto recebido; a completar.*

 * Fator de Majoração Dinâmica Combinado (F_D):

*Equação ou desenvolvimento ausente no texto recebido; a completar.*


### 5.4 Distribuição Transversal do Trem-Tipo TB-450 na Longarina L1

Adota-se o modelo da alavanca transversal para determinar a Linha de Influência da Reação de Apoio na Longarina L1 (\eta_1(x)).
 * Posição de L1: $x = 0{,}00\text{ m}$ \rightarrow \eta_1(0) = $1{,}00$.
 * Posição de L2: $x = 5{,}00\text{ m}$ \rightarrow \eta_1(5) = $0{,}00$.
 * Bordo Esquerdo da Laje: $x = -2{,}00\text{ m}$ \rightarrow \eta_1(-2) = 1 + \frac{$2{,}00$}{$5{,}00$} = $1{,}40$.

```text
     1.40
      | \
      |  \  1.00
      |   \  |
```

 -----+----+--+-------------------------+----- (Tabuleiro Transversal)
    -2m   -1.6m 0m                     5m

```text
            \   |                      |
             \  |                      |
              \ L1                     L2
```



#### Posicionamento Crítico do Veículo TB-450


O veículo TB-450 é posicionado encostado na barreira esquerda da pista ($x = -1{,}60\text{ m}$):
 * Roda 1 (Esquerda): Posicionada em x_1 = $-1{,}60\text{ m}$.
   
 * Roda 2 (Direita): Posicionada em x_2 = $-1{,}60$ + $2{,}00$ = +$0{,}40\text{ m}$.
   

#### Carga Concentrada do Eixo na Longarina L1


Cada eixo do TB-450 possui $150\text{ kN}$ ($75\text{ kN}$ por roda):

*Equação ou desenvolvimento ausente no texto recebido; a completar.*

Majorando pelo fator dinâmico F_D = $1{,}6034$:


#### Carga Distribuída de Multidão na Longarina L1


A multidão $q = 5{,}0\text{ kN/m}^2$ atua no trecho de ordenadas positivas da LI Transversal (de $x = -2{,}00\text{ m}$ até x = +$5{,}00\text{ m}$):

*Equação ou desenvolvimento ausente no texto recebido; a completar.*

Carga equivalente não majorada por metro linear na longarina:

*Equação ou desenvolvimento ausente no texto recebido; a completar.*

Majorando pelo fator dinâmico F_D = $1{,}6034$:

*Equação ou desenvolvimento ausente no texto recebido; a completar.*


### 5.5 Resumo das Ações de Cálculo para o Dimensionamento Longitudinal

Para o projeto da Longarina L1 no vão de $25{,}00\text{ m}$, as ações finais de cálculo a serem consideradas no modelo longitudinal são:
 * Carga Permanente Uniforme: $g_{\text{long}} = 57{,}31\text{ kN/m}$.
 * Trem-Tipo Longitudinal Majorado:
   * 3 Cargas Concentradas de Eixo: $P_{\text{long, final}} = 269{,}37\text{ kN}$ cada (espaçadas de $1{,}50\text{ m}$).
   * Carga Distribuída Contínua de Multidão: $q_{\text{long, final}} = 39{,}28\text{ kN/m}$.

## Referências

(ref-1)=
**[1]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 6118**: *Projeto de estruturas de concreto — Procedimento*. Rio de Janeiro: ABNT.

(ref-2)=
**[2]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 7187**: *Projeto de pontes de concreto armado e de concreto protendido — Procedimento*. Rio de Janeiro: ABNT, 2003.

(ref-3)=
**[3]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 7188**: *Carga móvel rodoviária e de pedestres em pontes, viadutos, passarelas e outras estruturas*. Rio de Janeiro: ABNT, 2013.

(ref-4)=
**[4]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 6120**: *Cargas para o cálculo de estruturas de edificações*. Rio de Janeiro: ABNT.

(ref-5)=
**[5]** DEPARTAMENTO NACIONAL DE INFRAESTRUTURA DE TRANSPORTES (DNIT). *Manual de Projetos de Obras d'Arte Especiais* (DNIT 698). Brasília, 1996.
