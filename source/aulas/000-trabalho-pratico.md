# **Trabalho Prático**

## 1. Diretrizes de projeto

O trabalho prático do semestre consiste no dimensionamento de uma ponte de concreto armado com duas longarinas moldadas *in loco*. Será tomada como referência a ponte que consta na bibliografia de Marchetti [[1]](#ref-1), cujo corte longitudinal é apresentado na [Figura 1](#fig-1).

(fig-1)=
```{figure} ../_static/aulas/ponte-referencia.png
:alt: Corte longitudinal da ponte de referência
:width: 80%

**Figura 1** – Corte longitudinal da ponte de referência, com vão central de 25,00 m, balanços de 4,50 m, pilares de 12,00 m e sapatas de 3,00 m x 1,35 m.
```

O projeto de fôrma completo da ponte de referência (plantas, cortes e detalhamento) está disponível para download em {download}`trabalho.pdf <../_static/arquivos/ponte-referencia.pdf>`.

### 1.1 Parâmetros base do projeto

- Vão principal (central): $25{,}00\text{ m}$
- Balanços: $4{,}50\text{ m}$
- Altura dos pilares: $12{,}00\text{ m}$ (diâmetro/largura de $1{,}20\text{ m}$)
- Fundação em Tubulão de Concreto Armado
- Concreto: $f_{ck} = 30\text{ MPa}$
- Aço: CA-50 ($f_{yk} = 500\text{ MPa}$)
- Cobrimento nominal: $c_{\text{nom}} = 4\text{ cm}$
- Classe de agressividade ambiental: CAA III (forte / industrial ou marinha)

## 2. Roteiro de etapas e entregas do semestre

### 2.1 Desenho da estrutura e das seções transversais em CAD

- Lançamento da geometria da ponte em CAD: Corte longitudinal, Corte B, Corte C, Detalhe 1 e Detalhe 5.

```{admonition} Detalhe 5: Barreira New Jersey
:class: destaque-vermelho

Para o Detalhe 5, a barreira tipo New Jersey deverá ser representada conforme os detalhes do *Manual de projeto de obras-de-arte especiais*, do DNER, Publicação IPR 698 [[3]](#ref-3), substituindo a configuração apresentada no desenho de referência.
```

### 2.2 Levantamento de carregamentos permanentes

- Peso próprio das longarinas, laje do tabuleiro, mísulas e transversinas ($\gamma_c = 25\text{ kN/m}^3$).
- Peso da pavimentação em CBUQ: considerar peso específico de $\gamma_{\text{asf}} = 24\text{ kN/m}^3$ e espessura média inicial de $8\text{ cm}$, acrescido de uma carga permanente de $2\text{ kN/m}^2$ sobre a área pavimentada para previsão de recapeamento futuro.
- Peso das barreiras de proteção tipo New Jersey (Detalhe 5) e guarda-corpos metálicos com peso linear de $0,10\text{ kN/m}$.

### 2.3 Cálculo dos esforços permanentes

- Determinação da carga permanente distribuída $g_{\text{long}}$ por metro linear em cada longarina.
- Modelo estrutural contínuo/isostático considerando a geometria longitudinal (vão central de $25\text{ m}$ e balanços/extensões de $4{,}5\text{ m}$ e $3{,}0\text{ m}$).
- Obtenção dos diagramas de momentos fletores ($M_g$) e esforços cortantes ($V_g$) ao longo do comprimento das vigas para a carga permanente.

```{admonition} Entrega 1: Desenhos e carregamentos permanentes
:class: destaque-verde

A **Entrega 1** contempla os itens **2.1, 2.2 e 2.3** do roteiro de projeto.

**Item 2.1 - Desenhos em AutoCAD:** desenvolver as seções transversais e os detalhes necessários para determinar o peso das peças de concreto da ponte de referência.

**Item 2.2 - Carregamentos permanentes:** determinar as áreas e os volumes das peças desenhadas em AutoCAD e calcular os carregamentos permanentes que atuam sobre a ponte, incluindo os demais componentes previstos neste item.

**Item 2.3 - Análise de esforços no Ftool:** representar o sistema estrutural da ponte, aplicar os carregamentos permanentes calculados e determinar os diagramas de momentos fletores e esforços cortantes na longarina.

**Apresentação e arquivos obrigatórios:**

- Entregar os desenhos em arquivo **DWG compatível com o AutoCAD 2020**, com layouts e **viewports configuradas para plotagem**, escalas definidas e enquadramento adequado.
- Entregar também as **versões em PDF de todas as pranchas**, correspondentes aos layouts do DWG, com textos, cotas e detalhes legíveis no tamanho de impressão previsto.
- Entregar a **memória de cálculo em PDF**, com áreas, volumes, pesos específicos, carregamentos e resultados da análise, e o **arquivo editável do modelo no Ftool**.
- Identificar todas as pranchas e a memória de cálculo com **nome completo e matrícula de todos os integrantes**, identificação da entrega e do projeto.
- Numerar as pranchas em sequência, indicando o número da prancha e o total, por exemplo, **01/03, 02/03 e 03/03**.
- Incluir **notas de projeto quando necessárias**, esclarecendo unidades, materiais, hipóteses, convenções e informações necessárias à interpretação dos desenhos e cálculos.
- Organizar e nomear os arquivos de modo que seja possível identificar o grupo, o conteúdo e a prancha correspondente. Conferir se todos os arquivos abrem e se as referências externas necessárias estão incluídas.

**Critérios de avaliação da Entrega 1 (10,0 pontos):**

| Critério | O que será avaliado | Pontuação máxima |
|---|---|---:|
| Organização das pranchas | Distribuição dos desenhos, alinhamento, uso do espaço e organização do carimbo. | 1,0 |
| Numeração das pranchas | Sequência completa, indicação do total e correspondência entre DWG e PDF. | 0,5 |
| Legibilidade e plotagem | Leitura de textos, cotas e detalhes; escalas, espessuras de linha e viewports; ausência de cortes e sobreposições no PDF. | 1,5 |
| Identificação e notas de projeto | Nome completo e matrícula de todos os integrantes, identificação do projeto e notas necessárias à compreensão. | 1,0 |
| Arquivos entregues | DWG compatível com AutoCAD 2020, PDFs de todas as pranchas, memória de cálculo em PDF e modelo editável do Ftool, completos e acessíveis. | 1,0 |
| Desenhos e detalhes técnicos | Atendimento ao item 2.1, geometria, cotas e adequação do Detalhe 5 ao manual indicado. | 2,0 |
| Carregamentos permanentes | Áreas, volumes, unidades, pesos específicos e determinação dos carregamentos previstos no item 2.2. | 1,5 |
| Modelo e esforços no Ftool | Geometria, apoios, aplicação dos carregamentos e diagramas de momentos fletores e esforços cortantes na longarina. | 1,5 |
| **Total** | | **10,0** |

**Regra de pontuação:** cada critério recebe 100% dos pontos quando atendido integralmente, 50% quando atendido parcialmente e zero quando ausente, incorreto ou impossível de verificar. A falta de identificação completa de todos os integrantes zera o critério de identificação e notas. Arquivos ausentes ou que não abrem não pontuam no conteúdo que depender deles para ser verificado. A ausência de notas de projeto não gera desconto quando elas não forem necessárias. A nota final corresponde à soma dos critérios.
```

### 2.4 Levantamento de carregamentos variáveis

**Ações variáveis ($q$):**

- Veículo-tipo normativo TB-450 (ABNT NBR 7188:2024 [[2]](#ref-2)): 3 eixos de $150\text{ kN}$ ($75\text{ kN}$ por roda) espaçados em $1{,}50\text{ m}$.
- Carga distribuída de multidão: $q = 5{,}0\text{ kN/m}^2$ na pista de rolamento.
- Carga nos passeios para pedestres: $3{,}0\text{ kN/m}^2$ concomitante ou $5{,}0\text{ kN/m}^2$ para dimensionamento local.

**Coeficientes dinâmicos:**

- Coeficiente de Impacto Vertical (CIV) — conforme ABNT NBR 7188:2024 [[2]](#ref-2).
- Coeficiente de Número de Faixas (CNF) — conforme ABNT NBR 7188:2024 [[2]](#ref-2).
- Coeficiente de Impacto Adicional ($CIA = 1{,}25$ para estruturas de concreto).
- Fator dinâmico combinado: $F_D = CIV \cdot CNF \cdot CIA$.

### 2.5 Cálculo dos esforços do trem-tipo

- Construção das linhas de influência (LI) para momentos fletores e esforços cortantes nas seções críticas ($L/8$, $L/4$, $3L/8$, $L/2$ e sobre os apoios).
- Determinação do trem-tipo transversal simplificado (método da alavanca ou grelha) para definir a parcela de carga transferida para a longarina mais solicitada.
- Posicionamento longitudinal do veículo TB-450 e da carga de multidão sobre as LI para obter os esforços máximos e mínimos.
- Majoração de todos os esforços móveis pelo fator dinâmico $F_D$.

### 2.6 Envoltória final de esforços

- Combinação de ações no Estado Limite Último (ELU), conforme NBR 7187 e NBR 6118, utilizando $\gamma_g = 1{,}35$ para ações permanentes e $\gamma_q = 1{,}50$ para ações variáveis.
- Traçado dos diagramas envoltórios de flexão ($M_{sd,\text{máx}}$ e $M_{sd,\text{mín}}$) e de cortante ($V_{sd,\text{máx}}$).

### 2.7 Dimensionamento da longarina com verificação à fadiga

**Dimensionamento à flexão (ELU):**

- Cálculo da armadura longitudinal $A_s$ para atender aos momentos $M_{sd,\text{máx}}$ ao longo da viga.
- Verificação da capacidade resistente da seção em "T" ou retangular.

**Dimensionamento ao cisalhamento (ELU):**

- Verificação da compressão diagonal do concreto ($V_{sd} \le V_{rd2}$).
- Cálculo dos estribos $A_{sw}/s$ (modelo de cálculo I ou II da NBR 6118).

**Verificação à fadiga (ELS-FAT):**

- Determinação da variação da tensão no aço ($\Delta \sigma_s$) decorrente da passagem do veículo-tipo.
- Verificação da tensão máxima no concreto sob a combinação de fadiga ($\sigma_c \le 0{,}45 \cdot f_{ck}$).

### 2.8 Dimensionamento da transversina

- Análise do comportamento estrutural das transversinas localizadas sobre os pilares/apoios e no vão intermediário.
- Avaliação dos esforços de flexão, torção e cisalhamento induzidos pela rigidez transversal do tabuleiro.
- Verificação dos esforços decorrentes do macaqueamento (operação de elevação do tabuleiro para substituição dos aparelhos de apoio).
- Dimensionamento da armadura longitudinal superior, inferior e estribos das transversinas.

### 2.9 Dimensionamento do tabuleiro (laje)

- Divisão da laje nas regiões: laje central (viga contínua apoiada nas longarinas) e laje em balanço.
- Cálculo da difusão das cargas concentradas das rodas do veículo TB-450 a $45^\circ$ através da camada de asfalto e da espessura da laje.
- Determinação dos momentos fletores locais ($M_x$ e $M_y$) utilizando tabelas de lajes (Rüsch/Pucher) ou o método das faixas equivalentes.
- Dimensionamento da armadura principal (transversal ao tráfego) e armadura de distribuição/secundária (longitudinal ao tráfego).

### 2.10 Forças horizontais

- **Frenagem e aceleração:** maior valor entre 25% do peso do veículo-tipo ($0{,}25 \times 450\text{ kN} = 112{,}5\text{ kN}$) ou 5% da carga total de multidão na pista utilizável.
- **Ação do vento:** pressão característica do vento aplicada à área projetada lateral da superestrutura (com e sem tráfego).
- **Variação térmica e retração/fluência:** avaliação do deslocamento horizontal de origem térmica ($\Delta T$) transmitido aos apoios e ao topo dos pilares.

### 2.11 Dimensionamento dos pilares e infraestrutura

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

(ref-2)=
**[2]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. *ABNT NBR 7188: Ações devido ao tráfego de veículos rodoviários e de pedestres em pontes, viadutos e passarelas*. Rio de Janeiro: ABNT, 2024.

(ref-3)=
**[3]** BRASIL. Departamento Nacional de Estradas de Rodagem. Diretoria de Desenvolvimento Tecnológico. Divisão de Capacitação Tecnológica. *Manual de projeto de obras-de-arte especiais*. Rio de Janeiro: DNER, 1996. 225 p. (Publicação IPR, 698). Disponível em: [acervo de manuais do DNIT](https://www.gov.br/dnit/pt-br/assuntos/planejamento-e-pesquisa/ipr/coletanea-de-manuais/vigentes/698_manual_de_projeto_de_obras_de_arte_especiais.pdf). Acesso em: 8 set. 2026.
