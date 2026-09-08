# **Trabalho Prático**

## Diretrizes de projeto

O trabalho prático do semestre consiste no dimensionamento de uma ponte de concreto armado com duas longarinas moldadas *in loco*. Será tomada como referência a ponte que consta na bibliografia de Marchetti [[1]](#ref-1), cujo corte longitudinal é apresentado na [Figura 1](#fig-1).

(fig-1)=
```{figure} ../_static/aulas/ponte-referencia.png
:alt: Corte longitudinal da ponte de referência
:width: 80%

**Figura 1** – Corte longitudinal da ponte de referência, com vão central de 25,00 m, balanços/vãos laterais de 4,50 m e 3,00 m, pilares de 12,00 m e sapatas de 3,00 m x 1,35 m.
```

O projeto completo da ponte de referência (plantas, cortes e detalhamento) está disponível para download em {download}`ponte-referencia.pdf <../_static/arquivos/ponte-referencia.pdf>`.

### Parâmetros base do projeto

- Vão principal (central): $25{,}00\text{ m}$
- Vãos laterais: $4{,}50\text{ m}$
- Altura dos pilares: $12{,}00\text{ m}$ (diâmetro/largura de $1{,}20\text{ m}$)
- Bloco de fundação / sapata: $3{,}00\text{ m} \times 1{,}35\text{ m}$ ($1{,}15\text{ m} + 0{,}20\text{ m}$)
- Concreto: $f_{ck} = 30\text{ MPa}$
- Aço: CA-50 ($f_{yk} = 500\text{ MPa}$)
- Cobrimento nominal: $c_{\text{nom}} = 4\text{ cm}$
- Classe de agressividade ambiental: CAA III (forte / industrial ou marinha)

### Roteiro de etapas e entregas do semestre

#### a) Desenho da estrutura e das seções transversais em CAD

- Lançamento da geometria da ponte em CAD: planta, corte longitudinal e seções transversais (no meio do vão e sobre os apoios), a partir dos parâmetros base do projeto.
- Detalhamento das longarinas, laje do tabuleiro, transversinas, pilares e sapatas, servindo de referência geométrica para as etapas seguintes.

#### b) Levantamento de carregamentos

**Ações permanentes ($g$):**

- Peso próprio das longarinas, laje do tabuleiro, mísulas e transversinas ($\gamma_c = 25\text{ kN/m}^3$).
- Peso da pavimentação em CBUQ ($\gamma_{\text{asf}} = 24\text{ kN/m}^3$, espessura média de $8\text{ cm}$), acrescido da reserva para recapeamento futuro ($2\text{ kN/m}^2$).
- Peso das barreiras de proteção tipo New Jersey ($0{,}23\text{ m}^2 \times 25\text{ kN/m}^3$ por bordo) e guarda-corpos metálicos.

**Ações variáveis ($q$):**

- Veículo-tipo normativo TB-450 (ABNT NBR 7188): 3 eixos de $150\text{ kN}$ ($75\text{ kN}$ por roda) espaçados em $1{,}50\text{ m}$.
- Carga distribuída de multidão: $q = 5{,}0\text{ kN/m}^2$ na pista de rolamento.
- Carga nos passeios para pedestres: $3{,}0\text{ kN/m}^2$ concomitante ou $5{,}0\text{ kN/m}^2$ para dimensionamento local.

**Coeficientes dinâmicos:**

- Coeficiente de Impacto Vertical (CIV) — conforme ABNT NBR 7188.
- Coeficiente de Número de Faixas (CNF) — conforme ABNT NBR 7188.
- Coeficiente de Impacto Adicional ($CIA = 1{,}25$ para estruturas de concreto).
- Fator dinâmico combinado: $F_D = CIV \cdot CNF \cdot CIA$.

#### c) Cálculo dos esforços permanentes

- Determinação da carga permanente distribuída $g_{\text{long}}$ por metro linear em cada longarina.
- Modelo estrutural contínuo/isostático considerando a geometria longitudinal (vão central de $25\text{ m}$ e balanços/extensões de $4{,}5\text{ m}$ e $3{,}0\text{ m}$).
- Obtenção dos diagramas de momentos fletores ($M_g$) e esforços cortantes ($V_g$) ao longo do comprimento das vigas para a carga permanente.

#### d) Cálculo dos esforços do trem-tipo

- Construção das linhas de influência (LI) para momentos fletores e esforços cortantes nas seções críticas ($L/8$, $L/4$, $3L/8$, $L/2$ e sobre os apoios).
- Determinação do trem-tipo transversal simplificado (método da alavanca ou grelha) para definir a parcela de carga transferida para a longarina mais solicitada.
- Posicionamento longitudinal do veículo TB-450 e da carga de multidão sobre as LI para obter os esforços máximos e mínimos.
- Majoração de todos os esforços móveis pelo fator dinâmico $F_D$.

#### e) Envoltória final de esforços

- Combinação de ações no Estado Limite Último (ELU), conforme NBR 7187 e NBR 6118, utilizando $\gamma_g = 1{,}35$ para ações permanentes e $\gamma_q = 1{,}50$ para ações variáveis.
- Traçado dos diagramas envoltórios de flexão ($M_{sd,\text{máx}}$ e $M_{sd,\text{mín}}$) e de cortante ($V_{sd,\text{máx}}$).

#### f) Dimensionamento da longarina com verificação à fadiga

**Dimensionamento à flexão (ELU):**

- Cálculo da armadura longitudinal $A_s$ para atender aos momentos $M_{sd,\text{máx}}$ ao longo da viga.
- Verificação da capacidade resistente da seção em "T" ou retangular.

**Dimensionamento ao cisalhamento (ELU):**

- Verificação da compressão diagonal do concreto ($V_{sd} \le V_{rd2}$).
- Cálculo dos estribos $A_{sw}/s$ (modelo de cálculo I ou II da NBR 6118).

**Verificação à fadiga (ELS-FAT):**

- Determinação da variação da tensão no aço ($\Delta \sigma_s$) decorrente da passagem do veículo-tipo.
- Verificação da tensão máxima no concreto sob a combinação de fadiga ($\sigma_c \le 0{,}45 \cdot f_{ck}$).

#### g) Dimensionamento da transversina

- Análise do comportamento estrutural das transversinas localizadas sobre os pilares/apoios e no vão intermediário.
- Avaliação dos esforços de flexão, torção e cisalhamento induzidos pela rigidez transversal do tabuleiro.
- Verificação dos esforços decorrentes do macaqueamento (operação de elevação do tabuleiro para substituição dos aparelhos de apoio).
- Dimensionamento da armadura longitudinal superior, inferior e estribos das transversinas.

#### h) Dimensionamento do tabuleiro (laje)

- Divisão da laje nas regiões: laje central (viga contínua apoiada nas longarinas) e laje em balanço.
- Cálculo da difusão das cargas concentradas das rodas do veículo TB-450 a $45^\circ$ através da camada de asfalto e da espessura da laje.
- Determinação dos momentos fletores locais ($M_x$ e $M_y$) utilizando tabelas de lajes (Rüsch/Pucher) ou o método das faixas equivalentes.
- Dimensionamento da armadura principal (transversal ao tráfego) e armadura de distribuição/secundária (longitudinal ao tráfego).

#### i) Forças horizontais

- **Frenagem e aceleração:** maior valor entre 25% do peso do veículo-tipo ($0{,}25 \times 450\text{ kN} = 112{,}5\text{ kN}$) ou 5% da carga total de multidão na pista utilizável.
- **Ação do vento:** pressão característica do vento aplicada à área projetada lateral da superestrutura (com e sem tráfego).
- **Variação térmica e retração/fluência:** avaliação do deslocamento horizontal de origem térmica ($\Delta T$) transmitido aos apoios e ao topo dos pilares.

#### j) Dimensionamento dos pilares e infraestrutura

**Solicitações nos pilares:**

- Carga vertical máxima $N_{sd}$ proveniente das reações de apoio das longarinas e peso próprio do pilar ($H = 12{,}00\text{ m}$, $\phi = 1{,}20\text{ m}$).
- Momento fletor $M_{sd}$ decorrente das forças horizontais de frenagem, vento e variações térmicas.

**Efeitos de 2ª ordem:**

- Verificação da esbeltez do pilar ($\lambda$) devido à altura livre de $12{,}00\text{ m}$ e consideração do momento fletor de segunda ordem ($M_{2d}$).

**Dimensionamento da armadura do pilar:**

- Utilização de diagramas de flexo-compressão oblíqua/reta para determinação da armadura longitudinal ($A_s$) e estribos em cinta/espiral.

**Verificação do bloco de fundação / sapata:**

- Verificação das tensões na base de assentamento do bloco/sapata ($3{,}00\text{ m} \times 1{,}35\text{ m}$) e dimensionamento da armadura de tração inferior.

## Referências

(ref-1)=
**[1]** MARCHETTI, Osvaldemar. *Pontes de Concreto Armado*. 2. ed. São Paulo: Blucher, 2018. 246 p. ISBN 978-85-212-1278-2.
