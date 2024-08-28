import re

def remover_linhas_com_timestamp(texto):
    # Expressão regular para encontrar o padrão de timestamp
    padrao = r'\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}'
    
    # Dividindo o texto em linhas
    linhas = texto.splitlines()
    
    # Filtrando as linhas que não contêm o padrão de timestamp
    linhas_filtradas = [linha for linha in linhas if not re.search(padrao, linha)]
    
    # Unindo as linhas filtradas de volta em um único texto
    texto_filtrado = "\n".join(linhas_filtradas)
    
    return texto_filtrado

# Exemplo de uso
texto = """
00:00:00.000 --> 00:00:03.000
Então eu acho que todos já estão sabendo a sinalização. O intuito dessa reunião. O intuito da reunião é apresentar pra vocês o sistema íris. E vou aproveitando também é que as.

00:00:03.000 --> 00:00:06.000
Ah, só minutinho, gente, gosto melhor. Todos estão me ouvindo?

00:00:06.000 --> 00:00:10.000
Não? Sim, é que eu coloquei pra gravar a reunião.

00:00:10.000 --> 00:00:19.000
Ah, tá. E pra falar sobre o sistema, ires sobre a implantação do sistema. Eles na casa, abrigo, e também ressaltar a importância do uso do sistema.

00:00:19.000 --> 00:00:26.000
Sei, tá bom, não é? Porque ele vai ter o íris que nós vamos deixar de usar o seio ou dar o pontapé.

00:00:26.000 --> 00:00:46.000
Iniciar. Não sei porque depois nós vamos tratar do C em outra situação e outra oportunidade. A princípio, é o principal ponto dessa reunião. A implantação do sistema Íris com o João. João. Vai dar vai ensinar pra gente você vai apresentar João.

00:00:46.000 --> 00:00:50.000
Senhor vai fazer apresentação.

00:00:50.000 --> 00:00:58.000
Não. Ótimo, só minutinho, gente.

00:00:58.000 --> 00:00:59.000
Ah, tá. Desculpa. Vou me apresentar. Eu sou a Valéria, coordenadora dos equipamentos e substituto da maíra Auxiliando.

00:00:59.000 --> 00:01:12.000
Aqui a paloma do sistema.

00:01:12.000 --> 00:01:13.000
Pode falar. Rodrigo.

00:01:13.000 --> 00:01:28.000
É bem antes do João falar, não é Rodrigo Marcelino. Estou como diretor aqui da da Diretora de Tecnologia da Secretaria da Mulher é o sistema só pra dar um.

00:01:28.000 --> 00:01:37.000
Ou iniciação. O sistema já é um sistema utilizado na casa da mulher brasileira de campo Grande através de um termo de cooperação.

00:01:37.000 --> 00:01:52.000
Em dois mil e vinte e dois, a Secretaria da Mulher, adquiriu o sistema. O implementamos o ano passado na casa da mulher brasileira.

00:01:52.000 --> 00:02:01.000
E como é um sistema que já foi testado, já está sendo anos testado na casa da mulher. Campo grande.

00:02:01.000 --> 00:02:12.000
E também já tem seis, sete meses que está sendo usado aqui na casa da mulher brasileira. A gente agora está começando a implementar nas outras unidades.

00:02:12.000 --> 00:02:23.000
Então a gente agora, após a casa da mulher brasileira, a gente tá começando pela casa abrigo. Depois gente vai passar para os nafados e depois para o cenas.

00:02:23.000 --> 00:02:35.000
Então o João é o nosso desenvolvedor. Ele vai estar mostrando o sistema pra vocês. E assim vamos combinar o seguinte.

00:02:35.000 --> 00:02:43.000
João, você prefere que interrompam e façam as perguntas ou deixa para perguntar. No final.

00:02:43.000 --> 00:02:50.000
Eu acho que se for algo muito pontual, a gente pode colocar para tirar essas dúvidas no final, mas também está aberto.

00:02:50.000 --> 00:02:56.000
Quiser interromper quando eu estiver falando, não tiver algum questionamento, alguma coisa pode ficar à vontade também.

00:02:56.000 --> 00:03:06.000
Ok, vamos combinar então que se puderem, escrevam na lá no chat e a gente vai estar fazendo a pergunta do final.

00:03:06.000 --> 00:03:15.000
Se for algo que precisa tirar dúvidas na hora já podem ligar lá, levantar a mãozinha que a gente para.

00:03:15.000 --> 00:03:21.000
E vocês fazem a pergunta: tá, mas não esqueçam de preencher a lista de presença.

00:03:21.000 --> 00:03:26.000
Está no chat.

00:03:26.000 --> 00:03:34.000
Tudo mesmo. Valeu primeiramente. Boa tarde a todos. Eu espero que todos estejam me ouvindo bem.

00:03:34.000 --> 00:03:48.000
Agradeço a participação de todos aqui. Eu acredito que grande maioria seja da casa, abrigo, mas não sei se tem alguém do Observatório da Subsecretaria de Proteção.

00:03:48.000 --> 00:03:54.000
E eu estou aqui em nome da Diretoria de Tecnologia pra agradecer vocês mais uma vez. Já peço desculpas.

00:03:54.000 --> 00:03:58.000
Na época do meio dia.

00:03:58.000 --> 00:04:10.000
Para a câmara, porque a câmara ficou do outro lado. Aqui fica melhor para eu ver. Tá? O intuito dessa reunião aqui é a gente bater um papo inicial, tá?

00:04:10.000 --> 00:04:20.000
Sobre como funciona o sistema íris, como que ele é utilizado hoje na casa da mulher brasileira. Eu vou compartilhar minha tela aqui.

00:04:20.000 --> 00:04:27.000
Se você puder parar o seu compartilhamento Rodrigo. Ah, beleza. Já aparecendo para mim.

00:04:27.000 --> 00:04:35.000
Eu não. Não sei se vocês estão conseguindo ver. Eu não.

00:04:35.000 --> 00:04:36.000
Na cinta compartilhada.

00:04:36.000 --> 00:04:38.000
Está aparecendo até onde eles.

00:04:38.000 --> 00:04:39.000
Sim.

00:04:39.000 --> 00:04:50.000
Beleza. Então, voltando o intuito principal, aqui é a gente trocar uma ideia. Eu não sei se tem servidores técnicos aqui.

00:04:50.000 --> 00:05:07.000
Agente social, psicólogo, cuidador da casa, amigo. Vai ser importante. Essa nossa comunicação, para que vocês possam nos ajudar a paralisar o sistema de acordo com a necessidade de você.

00:05:07.000 --> 00:05:37.000
Tá ok. Nós já tínhamos uma documentação da Casabi dos formulários dos tipos de documentos que vocês coletam das mulheres abrigadas, acolhidas, aí, e nós conseguimos construir um esboço do que será entregue a vocês tá tivemos a reunião com a renata ela passou pra gente um pouco das responsabilidades e de como funciona hoje os atendimentos na casa abrigo então foi importante pra gente ter uma

00:05:41.000 --> 00:05:43.000
noção de como funciona mais ou menos a casa hoje. Eu peço pra que vocês fiquem tranquilos.

00:05:43.000 --> 00:05:56.000
Tá? Essa reunião aqui é somente um alinhamento. Um bate papo. A gente já tem todo um cronograma estabelecido.

00:05:56.000 --> 00:06:08.000
Vocês terão treinamentos presenciais. Você esperando um período de homologação para poder validar e aprovar as mudanças no sistema, sugerir melhorias.

00:06:08.000 --> 00:06:18.000
Gerente, novas implementações. Então não vai ser um processo. Repentino. E vocês não vão ser pegos de surpresa.

00:06:18.000 --> 00:06:29.000
De todo modo a detectar, vai estar sempre à disposição nesse período, tanto pelo Whatsapp quanto pelo portal de chamados pelo e mail, para que vocês entrem em contato com a gente beleza.

00:06:29.000 --> 00:06:32.000
Então, vamos lá. Como o Rodrigo já disse, Willis já está sendo utilizado na casa da Mulher Brasileira.

00:06:32.000 --> 00:07:02.000
Nossa aqui no Distrito Federal. Já tem mais ou menos sete meses. O pessoal está utilizando efetivamente, então, hoje a gente está mais ou menos o número para que vocês tenham uma ideia hoje, a gente já tem mais ou menos menos de oito cem mulheres cadastradas dentro do íris produção que é o nosso ambiente oficial com dados oficiais e sigilosos dos atendimentos que são feitos na casa Abril, o que eu vou apresentar para vocês aqui é

00:07:08.000 --> 00:07:35.000
um ambiente de teste. Tá de homologação que a gente construiu para o cenário da casa, abrigo, todos os dados que estão aqui são fictícios, até por conta do sigilo e confidencialidade dessas informações vou mostrar um pouquinho, do passo a passo e a gente vai trocando ideia no período tá eu espero que vocês estejam vendo aqui na minha tela azul que eu estou compartilhando essa aqui, é a

00:07:35.000 --> 00:07:45.000
tela inicial no sistema. Vocês também vão receber os acessos de vocês, tanto no ambiente de teste quanto no ambiente oficial.

00:07:45.000 --> 00:08:05.000
Hoje sou administrador do sistema. Então eu libero essas permissões. A gente cria usuários. A gente define as questões sigilosas de acordo com o que precisarem, vocês possam ter acesso a tela inicial no sistema.

00:08:05.000 --> 00:08:14.000
Vocês estão conseguindo ver bem pelo que nos captamos da documentação de requisitos da Casa Branca, nos conseguimos identificar.

00:08:14.000 --> 00:08:26.000
Que vocês são divididos em duas responsabilidades. Basicamente, tem o setor de acolhimento e o acompanhamento especializado.

00:08:26.000 --> 00:08:27.000
Nós temos os formulários de vocês e todos esses formulários já estão implementados aqui dentro.

00:08:27.000 --> 00:08:36.000
Para que vocês possam fazer os atendimentos. Tá ok. Questão de nomenclatura, questão de acesso. Questão de perfil. Tudo isso.

00:08:36.000 --> 00:08:52.000
Vocês vão ter o tempo para poder validar e me dizer se. Se a gente precisa alterar se, precisa implementar algo novo, então o ideal é que vocês entendam como o sistema.

00:08:52.000 --> 00:09:09.000
Funcionam soluções inteligentes aqui dentro, tá? Esse meu usuário que a Maria tem permissão tanto no acolhimento como no acompanhamento especializado e pelo que eu pude identificar, esse não é um cenário que acontece na casa.

00:09:09.000 --> 00:09:18.000
Abrigo enchido pelo psicólogo especialista. É sigiloso. E somente os psicólogos têm acesso a aquela informação. Já.

00:09:18.000 --> 00:09:25.000
O que é realizado no acolhimento e o agente social pelo cuidador. Enfim, é de acesso de toda a casa.

00:09:25.000 --> 00:09:40.000
Então é mais ou menos esse cenário que a gente construiu aqui dentro. Essa pessoa tem acesso aos dois perfis, mas esse aqui vai ser alterado conforme a necessidade de vocês se aplicar aqui no acolhimento, vocês estão conseguindo ver minha tela né?

00:09:40.000 --> 00:09:44.000
Rodrigo, você vai me guiando aí? Por favor?

00:09:44.000 --> 00:09:45.000
Ok, tá tudo certo.

00:09:45.000 --> 00:09:57.000
Eh, beleza. A gente tem essa tela inicial que o sistema. As operações dele são bem simples. Os nomes coloridos aqui embaixo.

00:09:57.000 --> 00:10:26.000
Vou explicar pra vocês que cada um desses nomes significa a gente tem várias colorações diferentes. Aqui temos um calendário aqui do lado que você pode selecionar a data e ver os atendimentos do dia que aconteceram naquele dia, em várias datas e nada está aparecendo para mim nesse quadrado branco porque esses cadastros foram todos inseridos em um dia, só para poder mostrar para vocês se não me engano foi aqui no dia,

00:10:26.000 --> 00:10:34.000
vinte e dois. Beleza. Então vocês estão vendo que a tela já mudou? Gente consegue ver os nomes das pessoas.

00:10:34.000 --> 00:10:46.000
Consegue ver a casa no nosso caso. A casa teste, homologação, a data, a hora, o número desse atendimento e aqui no lado, a gente tem um histórico, tá?

00:10:46.000 --> 00:11:16.000
Qual que e o grande ponto de se implementar o sistema. E além da gente ter todos os prontuários digitalizados com todos os anexos que vocês precisarem, a gente consegue também mapear o histórico dessa pessoa então se ela passou pela casa da mulher brasileira quando ela veio aqui, para casa, abrigo eu consigo consultar o histórico ter o acesso à informação por onde ela passou obviamente governo questões que não são

00:11:20.000 --> 00:11:22.000
sigilosas, e todo mundo começa a conversar. Mesmo em língua, em fazer encaminhamentos para onde tiver que fazer.

00:11:22.000 --> 00:11:37.000
E a gente consegue extrair esses dados com precisão. Tá? E aí dúvidas que forem surgindo. Tua disposição também.

00:11:37.000 --> 00:11:48.000
Então, beleza gente tem nesse campo central que todos esses nomes dessas pessoas que foram atendidas nesse dia, ele vai abrir pra mim uma tela.

00:11:48.000 --> 00:12:01.000
Eu tenho aqui acesso ao prontuário dessa pessoa. Vocês podem ver que o número que é bem pequeno está treze e dois, porque esse ambiente está zerado zero.

00:12:01.000 --> 00:12:11.000
A gente tem acesso aos dados iniciais como Cpf, a idade, o telefone, o nome, o nome social dessa pessoa mais aqui embaixo.

00:12:11.000 --> 00:12:14.000
A gente tem dados pertinentes ao atendimento com a data hora, o status e o número desse atendimento.

00:12:14.000 --> 00:12:44.000
Vocês podem utilizar esse atendimento para buscar informações. Depois, o local da ocorrência, quando foi inserido. Nesse caso, que não tem nada, porque a gente não inseriu nada nessa informação e aqui que vem a parte interessante os andamentos, então a gente tem o ar vou dar um pouco de zuma aqui pra ficar melhor pra vocês para que a gente tenha o acompanhamento especializado e o acolhimento então nessa tela que vocês vão ter acesso a todo o

00:12:51.000 --> 00:13:07.000
histórico dessa pessoa por onde ela passou. E todas as informações que foram coletadas. Parlamento especializado. Essas informações estão aparecendo porque não são sigilosas aqui, nesse modelo que a gente construiu, tá?

00:13:07.000 --> 00:13:11.000
Quem vai dizer para gente o que é sigiloso ou não, é a área de negócio. É a casa, amigo.

00:13:11.000 --> 00:13:20.000
Então, a gente consegue consultar as informações aqui. Esse formulário foi preenchido pela Maria Familiar.

00:13:20.000 --> 00:13:27.000
As respostas que foram preenchidas naquele questionário. Se a gestante se realiza pré natal.

00:13:27.000 --> 00:13:35.000
E eu posso vir aqui em outras informações. Tá? Uma vez. Tem poucas informações aqui.

00:13:35.000 --> 00:13:40.000
Porque é a nível de teste, mas vai estar disponível para que vocês possam preencher também beleza.

00:13:40.000 --> 00:13:42.000
Fechei aqui.

00:13:42.000 --> 00:13:49.000
Pagamento especializado. Posso ir lá no acolhimento também. Então, aqui eu tenho as informações do acolhimento, e esses.

00:13:49.000 --> 00:14:00.000
Esses andamentos vão aumentando com fome. Ela é atendida e passa por outros locais dentro da secretaria. Mesmo.

00:14:00.000 --> 00:14:15.000
Ok, o que são esses nomes aqui embaixo? Essas cores aqui, por que está desse formato aqui? Todos esses nomes que estão aparecendo aqui na minha tela é porque são pertinentes ao meu.

00:14:15.000 --> 00:14:24.000
Setor tá? Por que eu coloco entre aspas pelo que a gente já conversou com a Renata, não existe.

00:14:24.000 --> 00:14:53.000
Essa construção de setores dentro da casa abrigo, tá? Mas a gente precisa construir isso aqui dentro para dividir responsabilidades, justamente pra dizer quais são as responsabilidades do psicólogo e quais são as responsabilidades do agente social por isso que a gente tem o acolhimento e o acompanhamento especializado então todas as mulheres todas as pessoas atendidas que chegam aqui para mim no acolhimento que é o meu

00:14:53.000 --> 00:15:08.000
setor. Elas vão aparecer esse nome aqui embaixo tanto. Se ela vier encaminhado de outro equipamento ou até mesmo do setor dentro da casa abrigo. Quanto quando ela chega para mim, eu faço o cadastro.

00:15:08.000 --> 00:15:15.000
E começam atendê lo aqui no meu setor. Tá ok. Aqui a gente tem umas legendas também.

00:15:15.000 --> 00:15:27.000
Que explica um pouco melhor esses dois nomes vermelhos aqui é porque eu estou atendendo. Eu comecei a fazer o atendimento, mas ainda não finalizei e nem caminhei.

00:15:27.000 --> 00:15:28.000
Tá ok. Essas aqui que estão em roxo, é porque estão pendentes. Porque eu preciso atendê las.

00:15:28.000 --> 00:15:58.000
Porque provavelmente elas vieram encaminhadas de outro lugar para mim. Se eu passo que a tela, a gente tem também amarelo, que são os encaminhados, então essas pessoas foram atendidas aqui no acolhimento e foram encaminhadas, para algum lugar que lugar João aparece aqui o setor de destino doze h, cinco.

00:15:59.000 --> 00:16:02.000
Pessoas aqui. Elas foram encaminhadas.

00:16:02.000 --> 00:16:10.000
Acompanhamento especializado quando eu abri a tela do acompanhamento especializado, vocês vão ver que essas pessoas estão lá.

00:16:10.000 --> 00:16:23.000
Então essa tela, que foi construída justamente pra que vocês tenham essa noção de atendimentos de atendimentos, a fazer de atendimentos encaminhados e atendimentos finalizados.

00:16:23.000 --> 00:16:53.000
Esses aqui que estão verde foram os finalizados. Então significa o quê? A pessoa veio. Esteve aqui na casa abrigo e a gente finalizou esse atendimento dela, seja em um dia, ou seja, em treze dias ou dois meses, ou três meses, e por isso que eu vou precisar da ajuda de vocês para entender como que nos vamos construir isso de forma eficaz porque na casa, amigo, eu sei que geralmente as pessoas ficam o médio e longo período sendo abrigado

00:16:56.000 --> 00:17:26.000
pela casa. E vocês precisam fazer essas evoluções. Tá? Ok, então é um ponto que também eu acho interessante conversar com vocês quando eu estive na casa abrigo, a Renata me apresentou alguns modelos de documentação, de como que é feito essa evolução hoje, das pessoas que estão abrigadas, eu vi que vocês têm evolução, de plantão que vocês têm evolução ali do atendimento propriamente dito que ela me

00:17:28.000 --> 00:17:35.000
trouxe de uma pessoa em específico e dava mais ou menos umas duzentos e cinquenta folhas.

00:17:35.000 --> 00:17:46.000
Tá o nosso papel aqui. O papel da Diitec não é ser um complicador. A gente não tá aqui pra implementar a burocracia, tá?

00:17:46.000 --> 00:18:16.000
Muito pelo contrário, é importante que nós tenhamos essa comunicação nesse período, para que a gente consiga implementar com sucesso e que ele seja utilizado de fato, na prática, com vocês o que é atendimento ou o que não é atendimento até porque não somos especialistas, na ponta mas hoje, existe um conceito de atendimento, que é o que foi definido pela alta gestão, e que é o que a gente construiu aqui dentro, do sistema tá o atendimento propriamente

00:18:22.000 --> 00:18:35.000
dito é todo aquele fluxo. Quando uma pessoa entra ali, por exemplo, aqui no acolhimento, quando ela entra no acolhimento e o inicio, o atendimento dela.

00:18:35.000 --> 00:18:40.000
O atendimento. É aquele escopo que eu faço com ela. Então as evoluções que euicílio é o formulário que eu respondo.

00:18:40.000 --> 00:19:00.000
São os documentos que o anexo no prontuário dela. E quando eu faço algo, esse atendimento seja ou em caminho, ou finalizo aí sim, dentro do sistema, a gente contabiliza um atendimento.

00:19:00.000 --> 00:19:13.000
Que essa é um tema que a gente ainda vai conversar muito nas próximas reuniões. Tá ok. E o que vai vir para dentro do sistema é somente pertinente às pessoas e ao atendimento das pessoas.

00:19:13.000 --> 00:19:21.000
Então a evolução do plantão e demais informações, provavelmente vocês vão manter no escuro que já.

00:19:21.000 --> 00:19:37.000
E existe atualmente. Ok, vamos lá. Eu vou mostrar para vocês uma tela de atendimento. Eu tenho, por exemplo, essa pessoa que é um teste, é um dado teste.

00:19:37.000 --> 00:19:46.000
Se eu pico nesse Munique lateral, espero que vocês consigam ver. Eu posso clicar aqui para poder registrar no atendimento para essa pessoa.

00:19:46.000 --> 00:19:53.000
Eu venho aqui no salvar. E esse atendimento se inicia, tá ok.

00:19:53.000 --> 00:20:23.000
Vou fechar aqui novamente. Vou atualizar minha tela. Vocês podem ver que essa pessoa já ficou vermelho aqui, porque ela já está aqui para que eu o sistema já entende que eu estou atendendo abro aqui essa tela de atendimento e tenho aqui acesso ao formulário de vocês João de onde você tirou esse formulário dos documentos que nós temos da casa amigo tá é importante ressaltar o que todas essas

00:20:25.000 --> 00:20:38.000
nomenclaturas, essas permissões, essas perguntas, essas respostas, o sigilo, tudo isso é extremamente a gente pode e vai construir, conforme vocês passarem pra gente.

00:20:38.000 --> 00:21:03.000
Então, acho que essa pergunta não tem que estar aqui. Eu acho que a gente pode inserir isso aqui. Eu acho que a gente pode votar mais um tipo de formulário para que vá atender uma demanda específica, nossa, tá ok, a gente tá, aqui, pra isso tá, então talvez não sei, se tem alguém aqui, é a rede social, que é do acolhimento faz um acolhimento na casa, abrigo, mas aqui a gente eu vou dar

00:21:03.000 --> 00:21:13.000
umzinho. Aqui a gente tem a atualização do formulário que essa pessoa responde quando é atendida por um servidor do acolhimento.

00:21:13.000 --> 00:21:21.000
Então a gente tem várias questões específicas. Como escolas, se faz uso de drogas, se possuem deficiência.

00:21:21.000 --> 00:21:51.000
Tá e aqui as respostas também já foram criadas de acordo com o que existe no prontuário de lá nos documentos da casa, abrigo, um exemplo lá, vocês perguntam quais documentos a pessoa está apontando ali no ato do acolhimento então a gente já entrega aqui, também a certidão de nascimento certidão de casamento título eleitoral, carteira de trabalho e enfim, eu vou fazer vou responder aqui duas perguntas aqui só pra

00:21:54.000 --> 00:22:02.000
gente entender como a gente visualiza essa informação. Eu posso selecionar aqui, ou posso selecionar.

00:22:02.000 --> 00:22:08.000
Todas as questões.

00:22:08.000 --> 00:22:15.000
Então vou botar essa pessoa aqui como casada. E vou botar aquela porta aqui. A Certidão de Nascimento, beleza temos mais perguntas para baixo.

00:22:15.000 --> 00:22:34.000
Já deve ser do conhecimento de vocês. Salve esse atendimento. Tá ok, beleza. Se eu vir aqui no dia a dia.

00:22:34.000 --> 00:22:39.000
Atualizar lateral que tem a informação.

00:22:39.000 --> 00:22:50.000
Tranquilo. Vou voltar aqui nesse atendimento da Maria, tá? É uma informação ela. Vou preencher aqui novamente.

00:22:50.000 --> 00:23:03.000
Salvei. E, por exemplo, posso caminhar essa pessoa que lá pro acompanhamento especializado. Porque é outro setor que eu vou mostrar para vocês. Fiz um encaminhamento.

00:23:03.000 --> 00:23:06.000
Essa pessoa já tá lá. Ela some daqui.

00:23:06.000 --> 00:23:36.000
Tá? Dos meus atendentes. E ela vem para cá para os meus encaminhados. Eu sei que tem um cenário com vocês que é o seguinte: a pessoa fica ou um acolhimento ou um acompanhamento especializado por longos períodos então esse encaminhamento aqui não existiria aqui de imediato como que a gente faz nesse caso, aí a gente vai construir um local, onde vocês vão ter um canto pra inserir as evoluções

00:23:40.000 --> 00:24:10.000
técnicas ou evoluções administrativas que vocês precisarem. Essa pessoa pode ficar aqui sendo atendida pelo período também que for necessário então não é esse escopo fechado de que você tem que atender e encaminhar ou tem que atender e finalizar não você vai fazer o primeiro atendimento com ela vai preencher as informações e ela vai ficar aqui no acolhimento ou no acompanhamento especializado o tempo que for necessário Ah, e amanhã a gente precisa fazer uma evolução técnica beleza a gente vai ter um campo aqui pra que você

00:24:15.000 --> 00:24:34.000
entre lá no atendimento dela. Insira sua evolução e salve isso no histórico. Aí, quando você consultar o histórico dessa pessoa, vai estar lá.

00:24:34.000 --> 00:24:59.000
Então é as ações que nós podemos interferir aqui nesse momento inicial são essas, tá? A gente vai fazer o atendimento conforme o modelo que vocês suger uma coisa interessante de se falar tem uma grande diferença entre o a tela, de atendimento.

00:24:59.000 --> 00:25:09.000
Histórico ali que a gente vê as informações que foram preenchidas do prontuário. Aqui a gente tem os prontuários das pessoas.

00:25:09.000 --> 00:25:35.000
Então, o prontuário é como se fosse a maletinha que vocês têm hoje. A pasta daquela pessoa com as principais informações dela e os documentos dessa pessoa, como que a gente acessa essas informações primeiro eu posso pegar o nome de uma pessoa vou pegar o nome de uma pessoa que já está aqui na minha tela ou um cpf com um número de prontuário posso pesquisá la aqui nesse.

00:25:35.000 --> 00:25:43.000
Nesses campos que a gente tem aqui em cima, tá? Vou copiar e colar esse nome eu só apagar esse espaço que deu aqui. Pesquisei.

00:25:43.000 --> 00:26:05.000
Vocês conseguem ver que o nome dela apareceu aqui pra mim na tela, né? Então, o que acontece? Essa pessoa foi atendida no dia vinte e dois. Por isso que ela não estava aparecendo aqui para mim então às vezes você vai precisar consultar o histórico de alguma pessoa uma mulher chegou na casa, abrigo e você quer consultar aqui se ela já passou pela casa, abriu.

00:26:05.000 --> 00:26:12.000
Você pode vir aqui botar o nome dela e ver o histórico dessa pessoa. Opa, ela já passou por aqui.

00:26:12.000 --> 00:26:18.000
Deixa eu ver por quem que ela foi atendida. Ah, lá no acompanhamento, ela foi atendida pela Maria Beleza.

00:26:18.000 --> 00:26:46.000
Aí você pode iniciar um novo atendimento. Pode fazer uma nova evolução. E por aí em diante. Se eu pego o nome dessa pessoa e coloca aqui embaixo, vocês são vendo que aqui a gente tem nome, e aqui a gente também tem nome eu.

00:26:46.000 --> 00:26:57.000
Pesquisei aqui embaixo. Qual. Que é a grande diferença do João? Essa parte de baixo é pertinente aos atendimentos, aos andamentos dos atentados.

00:26:57.000 --> 00:27:22.000
Essa parte de cima é pertinente ao histórico da pessoa atendida. Aí ele me deu aqui que essa pessoa ainda está aqui para eu atender aqui no acolhimento. Então eu fiz um primeiro atendimento com ela e por algum motivo não fiz outro não dê prosseguimento e ela está aqui para ser atendido.

00:27:22.000 --> 00:27:27.000
Aqui desde o dia vinte e dois.

00:27:27.000 --> 00:27:34.000
Que vocês vão pegando mais habitualidade no dia a dia.

00:27:34.000 --> 00:27:44.000
Sobre os prontuários. E mais uma vez, tudo isso. A gente já tem construído em manuais. Vocês vão.

00:27:44.000 --> 00:27:49.000
Anuais. Então não se preocupem com isso. A gente tem esse botão.

00:27:49.000 --> 00:27:54.000
No canto que tem um íconezinho de um mais e de várias pessoas ele é para incluir um novo cadastro de uma pessoa.

00:27:54.000 --> 00:28:20.000
E aqui no atendimento também. Eu posso vir aqui em atendimento e colocar pessoa, tá? O que esse ícone que faz quando eu clico nele, ele me abre um campo de cadastro. Como vocês podem ver, são, bicho, acho que piscaram a tela aqui, como ele não.

00:28:20.000 --> 00:28:27.000
Só vou tirar aqui rapidinho.

00:28:27.000 --> 00:28:42.000
Beleza. Vamos lá. Como vocês podem ver, a gente tem uma tela de cadastro aqui, que são informações básicas iniciais. Pessoa a gente vai coletar essas informações, que é o prontuário.

00:28:42.000 --> 00:28:52.000
Te dito o nome. Nome social. Nome da mãe, data de nascimento, sexo, nacionalidade, naturalidade, raça ou cor etnia.

00:28:52.000 --> 00:28:57.000
Telefone. Um, dois, e mail Rg, órgão.

00:28:57.000 --> 00:29:10.000
E Cpf, vários documentos que na verdade, o Rg e o Cpf que estão aqui nesse formulário.

00:29:10.000 --> 00:29:40.000
Eles não são cantos obrigatórios. Gente já sabe que existem vários cenários em que, às vezes, uma mulher chega numa situação de ameaça ou de perigo ou de confusão, metal de trauma.

00:30:43.000 --> 00:31:09.000
Todas essas informações, elas ficam no prontuário dessa pessoa. O que outros servidores podem consultar e pegar essa informação que seja necessária. Então, que a gente tem uma aba dependentes que a gente pode pegar por exemplo, aqui, cadastrar os filhos dessa pessoa vou colocar o filho um de nove anos ele é frequente na escola frequenta a quinta série.

00:31:09.000 --> 00:31:20.000
Sei. Ele reside com vai. Os tios, por exemplo. Mas é só ver essa informação aqui.

00:31:20.000 --> 00:31:28.000
Eu já tenho o registro desse filho dessa pessoa que embaixo tá lá no formulário de vocês.

00:31:28.000 --> 00:31:41.000
Vocês também vão ter para poder cadastrar tanto os filhos que estão sendo abrigados ali no momento quanto os é que a gente tem uma água de contatos, tá eu posso cadastrar aqui a Joana um exemplo.

00:31:41.000 --> 00:31:53.000
Ela é uma amiga muito próxima dessa pessoa. Tá? Um contado de referência. Vou colocar um número de exemplo aqui, tá?

00:31:53.000 --> 00:32:05.000
Não é obrigado. Salvar o endereço dessa pessoa. Posso pegar e salvar ali a Joana como uma amiga. Posso salvar o Lucas como um tiro que é.

00:32:05.000 --> 00:32:15.000
Bastante próximo dessa pessoa e por aí, e aí por diante. Então a gente consegue que eu tenho um prontuário dessa pessoa.

00:32:15.000 --> 00:32:24.000
As informações básicas. Tem uma água de dependentes que eu posso tanto salvar. Esses dependentes quanto encaminhá los para um setor de brinquedoteca.

00:32:24.000 --> 00:32:32.000
Um exemplo, que é o que acontece hoje na casa da mulher brasileira. Posso cadastrar a rede de apoio ou contratos próximos.

00:32:32.000 --> 00:32:44.000
Com o pai, uma mãe, um tiro, uma avó, um primo. Temos aqui uma água que é bastante importante. Interessante, principalmente na casa abrigo que eu vi que vocês.

00:32:44.000 --> 00:32:55.000
Coletam muitos documentos e salvam muitos documentos para que nós já aproveitamos e construímos todas as categorias que vocês utilizam.

00:32:55.000 --> 00:33:23.000
Tá, que é a solicitação de desligamento. O termo de entrada termo de desligamento, materiais de uso durante o abrigamento rol de pertence controle do cofre, controle de ligações a evolução do plantão cheque list e aqui tem mais alguns outros que solicitação de medicação é o tema de advertência esse tempo de doação vocês podem por exemplo, eu não tem um documento

00:33:23.000 --> 00:33:34.000
que você imprime. Você assina você colhe a assinatura da pessoa. Você também é o próprio túnel.

00:33:34.000 --> 00:33:41.000
Pessoa dizer que é um termo de desligamento e escolher o arquivo que você está inserindo aqui.

00:33:41.000 --> 00:34:11.000
Tá esse arquivo vai ficar salvo aqui no prontuário dessa pessoa, tá? Então você pode acessar ele depois fazendo download anexar novos documentos, retirar esse documento ao invés da gente carregar uma pilha de de papéis a gente consegue ter esse cadastro aqui centralizado e comunicando com outros equipamentos bem grande bem âmbito para observações caso você precise inserir

00:34:13.000 --> 00:34:23.000
observações sobre essa pessoa, sobre esse atendimento ocorrência ou algo do tipo. Então é algo que vocês podem utilizar também.

00:34:23.000 --> 00:34:33.000
Mas todas as águas de atendimento já têm um campo de observação. Esse aqui foi um exemplo de uma pessoa já cadastrada.

00:34:33.000 --> 00:34:34.000
A gente vai!

00:34:34.000 --> 00:34:45.000
João. Aproveitando aqui essa parte aí, a Juliana lessa. Está perguntando se a solicitação de medicação trará registro de quem entregou o medicamento.

00:34:45.000 --> 00:34:48.000
Se a solicitação de medicação.

00:34:48.000 --> 00:34:56.000
E alguns. Alguns. Alguns documentos vão ser anexados e não vão ser inseridos aí.

00:34:56.000 --> 00:34:58.000
Vou tentando ser salvo antes de.

00:34:58.000 --> 00:35:05.000
No caso desta que ela está se a solicitação de medicação trará algum registro de quem entregou o medicamento?

00:35:05.000 --> 00:35:06.000
Tá.

00:35:06.000 --> 00:35:08.000
Essa solicitação de medicação é um daqueles anexos. Pode explicar pra ela?

00:35:08.000 --> 00:35:16.000
Vamos lá. Eu vou deixar bem explicado essa questão de anexo. Tá? Como que a gente procede aqui hoje dentro?

00:35:16.000 --> 00:35:45.000
A gente pode construir dentro do sistema um formulário específico pra medicação pode. A gente pode construir um formulário específico para medicação, onde você vai inserir o medicamento e outras informações que vocês precisam inserir tá ok, só que eu sei eu já vi que você já tem um documento pra isso onde você colhe a assinatura, dessa pessoa esses documentos que a gente precisa colher uma

00:35:45.000 --> 00:36:05.000
assinatura ou agente enquanto o servidor precisa assinar também. Eles não vão ser implementados dentro do sistema.

00:36:05.000 --> 00:36:15.000
Por assinatura que você imprime e tudo mais. Você pode digitalizar e subir aqui para o prontuário dessa pessoa.

00:36:15.000 --> 00:36:45.000
Fazer pronuncia ou para um e mail ou algum processo, às vezes do Ministério Público ou alguma coisa ao vivo de organização e a nível de controle, por que eu falo que a gente não vai implementar aqui justamente porque a gente não pode anular a importância de uma assinatura a punho do usuário da pessoa que está sendo acolhida principalmente quando se trata de questão de medicamento e como vocês já têm esses esse

00:36:47.000 --> 00:36:54.000
escopo. Construído esses documentos prontos. Não faz sentido. Não é viável que seja implementado aqui dentro.

00:36:54.000 --> 00:37:07.000
Mas se você precisarem que haja um ato do atendimento, a gente precisa coletar essas informações aqui, pertinente ao controle do cofre, ao controle do medicamento choro.

00:37:07.000 --> 00:37:13.000
Isso pode ser passado pra gente. E a gente vai pensar na solução mais viável de se fazer essa questão de documentação.

00:37:13.000 --> 00:37:27.000
É qual o documento do sei que faz parte do escopo do prontuário. Então você vai fazer. A pessoa vai assinar e você vai subir prontuário dessa pessoa.

00:37:27.000 --> 00:37:50.000
Respondendo a sua pergunta, se mostra ou não o nome daquela pessoa somente no documento. Se o documento tiver assinatura do servidor que fez ou o nome de quem fez beleza, mas é que, a nível de sistema, não eu posso manipular o prontuário, dessa pessoa e inserir esses documentos respondida para mim.

00:37:50.000 --> 00:37:57.000
Aí. Vai aparecer aí. Os documentos que ela tem anexado, né? Seja medicação, desligamento, etc.

00:37:57.000 --> 00:38:00.000
Exatamente.

00:38:00.000 --> 00:38:01.000
Exatamente.

00:38:01.000 --> 00:38:13.000
Aparece no prontuário da pessoa, os anexos, os documentos que foram anexados, aproveitando o João também. A Juliana pergunta, mas é ainda daquela primeira tela que você mostrou perguntando se tudo que é especializado é sigiloso.

00:38:13.000 --> 00:38:17.000
A acompanhamento especializado, provavelmente.

00:38:17.000 --> 00:38:33.000
Hum, eu acredito que é por causa daquelas duas Julianas. Pode explicar melhor. É por causa daqueles dois setores que a gente criou pra poder dividir o que é sigiloso, e não é.

00:38:33.000 --> 00:38:34.000
Boa tarde.

00:38:34.000 --> 00:38:37.000
Olá. Boa tarde. É o seguinte. Tem uma parte que é sigilosa, que eu compreendi.

00:38:37.000 --> 00:38:43.000
Por exemplo, quando o João citou que o acompanhar o atendimento no caso de um psicólogo que o psicólogo.

00:38:43.000 --> 00:38:53.000
Acho que a Cláudia até colocou essa pergunta mais na frente. Psicólogo tem dois tipos de atendimento que os outros especialistas realmente não podem ter acesso.

00:38:53.000 --> 00:38:54.000
E tem atendimento, pois não?

00:38:54.000 --> 00:38:58.000
Juliana. Mas isso é o que é hoje. É assim, né? Hoje, hoje tem psicólogo que registra.

00:38:58.000 --> 00:38:59.000
E isso exatamente.

00:38:59.000 --> 00:39:07.000
Tem o atendimento e. E tem outros psicólogos que não têm acesso. É isso.

00:39:07.000 --> 00:39:14.000
Não, não estou me referindo a isso porque o time de especialistas não se resume aos psicólogos.

00:39:14.000 --> 00:39:15.000
Uhum.

00:39:15.000 --> 00:39:24.000
Então existem algumas informações que os demais especialistas precisam acessar. Então não pode acessar aquilo que de fato é sigiloso para essa área da psicologia.

00:39:24.000 --> 00:39:44.000
Só que quando eu via a divisão. Me eu, que, no caso, eu, como especialista, pedagoga, teria acesso ao acolhimento ao documento de acolhimento e não ao de acompanhamento especializado. Se esse tiver sido realmente a intenção de colocar para os psicólogos só os psicólogos poderem acessar entende.

00:39:44.000 --> 00:39:49.000
Não. Não. Vamos lá. Qual que é a questão?

00:39:49.000 --> 00:39:57.000
Ainda vai ser definido com a Renata. E com os psicólogos. O que é sigiloso e o quer que não é.

00:39:57.000 --> 00:40:27.000
Isso é completamente flexível e completamente mutável. Redes sociais ou pedagogo, ou cuidador às vezes, ele precisa ter acesso a um prontuário do acompanhamento especializado para consultar alguma informação que não é sigilosa continuidade no atendimento dele, ou algo do tipo isso existe hoje no sistema servidores que são psicólogos que estão no acompanhamento especializado e dois servidores que são agentes sociais que estão no

00:40:30.000 --> 00:40:58.000
acolhimento. Ok, o que acontece? O que vai acontecer hoje? O que é sigiloso do psicólogo só é visto por quem está no setor dos psicólogos Washington vai tramitar por outros setores se for encaminhado o histórico dela vai estar aqui mas o que é sigiloso somente os psicólogos veem já no caso dos agentes sociais o que é feito o que é

00:40:58.000 --> 00:41:12.000
preenchido pelos agentes. É consultado. Fica disponível para ser consultado por toda a casa que passam pra gente que não tem que ser diferente.

00:41:12.000 --> 00:41:22.000
Os dois tem que ser sigiloso ou não, tem que ser sigiloso ajuda a gente construir. Mas o cenário hoje, é esse.

00:41:22.000 --> 00:41:25.000
Está respondido a sua pergunta?

00:41:25.000 --> 00:41:26.000
Oi, oi, oi.

00:41:26.000 --> 00:41:31.000
Eu não. Tchau, Renata. É que naquele dia, acho que a gente tá ouvindo? Está ouvindo?

00:41:31.000 --> 00:41:33.000
Tô te ouvindo. Tudo bem.

00:41:33.000 --> 00:41:47.000
Então é que naquela última reunião, a gente tinha decidido que os psicólogos, eles acessariam os dois, os dois.

00:41:47.000 --> 00:41:48.000
Certo.

00:41:48.000 --> 00:41:59.000
Os dois registros. E caso ele tivesse algo sigiloso, realmente que ele anotaria, não seria nesse local. Mas a casa teria acesso a pasta.

00:41:59.000 --> 00:42:00.000
Perfeito. Perfeito.

00:42:00.000 --> 00:42:10.000
Todo mundo, na mesma pasta. Só a questão do sigiloso que ficou tanto que eu já até mandei a lista pro Rodrigo sigiloso mesmo só seria do psicólogo.

00:42:10.000 --> 00:42:15.000
Perfeito.

00:42:15.000 --> 00:42:16.000
Beleza. Perfeito. Aí.

00:42:16.000 --> 00:42:18.000
Um fato ou outro que ele quiser registrar. Como? Acho que mais ou menos, fica bom assim.

00:42:18.000 --> 00:42:26.000
Ok aí, Juliana, dando continuidade na sua pergunta, é isso que a gente pode fazer dentro do setor do psicólogo.

00:42:26.000 --> 00:42:41.000
Acompanhamento especializado. E a gente vai ter um campo lá de questões sigilosas. Somente eles vem se não, todo o resto é consultavam pela casa, tá?

00:42:41.000 --> 00:42:57.000
Tá escondido.

00:42:57.000 --> 00:42:58.000
Exatamente exatamente exatamente. Beleza.

00:42:58.000 --> 00:43:04.000
Ah, entendi. Então, por acaso, eu, como especialista só aqui em pedagogia, eu acesso as informações do acolhimento especializado, e só não vou visualizar o que foi inserido ali dentro no caráter sigiloso dos psicólogos certo.

00:43:04.000 --> 00:43:09.000
Então vamos lá. Eu mostrei pra.

00:43:09.000 --> 00:43:10.000
Andréia.

00:43:10.000 --> 00:43:12.000
É João. Eu não sei se. Se Juliana, ele também respondeu a pergunta. Porque se perguntou?

00:43:12.000 --> 00:43:20.000
Também acho que precisamos um formulário de acompanhamento geral. Seria aquele prontuário que ele falou.

00:43:20.000 --> 00:43:25.000
Depois você está se referindo a outro formulário de acompanhamento geral.

00:43:25.000 --> 00:43:31.000
Não, não. Essa sugestão. No caso, só para o caso. Formulário especializado.

00:43:31.000 --> 00:43:44.000
Fica específico só para os psicólogos. Mas eu entendi o que ele colocou. O formulário especializado vai ser acessado por todos os especialistas.

00:43:44.000 --> 00:43:45.000
Ah, que.

00:43:45.000 --> 00:43:50.000
Exato. Exatamente, Andréia.

00:43:50.000 --> 00:43:51.000
André Crispim.

00:43:51.000 --> 00:43:59.000
Eu queria só tirar uma dúvida. João, sobre é me deu a sensação de quando você fala de acolhimento.

00:43:59.000 --> 00:44:05.000
Você está entendendo que são agentes sociais que fazem o acolhimento? É isso que você entendeu?

00:44:05.000 --> 00:44:27.000
Não é porque é o seguinte. E mais uma vez, eu quero deixar bem claro que questões de nomenclatura, divisões de responsabilidades vocês vão me passar o que vocês precisam.

00:44:27.000 --> 00:44:28.000
Não.

00:44:28.000 --> 00:44:45.000
Igual. A Juliana falou agora que ela é pedagoga. Eu não sabia que tinha essa especialidade dentro da casa, amigo, mas aí a gente pode construir um cenário específico, ou pode destinar um cenário específico essa questão do acolhimento é porque eu sei que existem os psicólogos que é o setor que precisa do sigilo que é o que foi passado pra gente e as outras especialidades já eram agentes

00:44:45.000 --> 00:44:46.000
Ah.

00:44:46.000 --> 00:44:52.000
sociais e os cuidadores. Se tem outras especialidades, também não há o menor problema da gente não tem o menor problema, entendeu?

00:44:52.000 --> 00:45:03.000
É isso. É bem importante. Até aproveito para te dizer. Então, agentes sociais, cuidadores.

00:45:03.000 --> 00:45:04.000
Legal.

00:45:04.000 --> 00:45:19.000
Técnicos administrativos estão todo mundo no nível de técnicos aqui, e as especialidades que que são direitos e legislação, pedagogia, educação social, serviço social e psicologia.

00:45:19.000 --> 00:45:20.000
Legal.

00:45:20.000 --> 00:45:34.000
Então e aí? É isso que Juliana também já explicou sobre os acessos. Então, no nível geral, todas as pessoas, todas nós, servidoras e servidores temos a responsabilidade com o sigilo.

00:45:34.000 --> 00:45:35.000
Exato. Exato.

00:45:35.000 --> 00:45:37.000
Colocou aqui as profissões que tem. O código de ética é importante, por isso é por conta de respeitar o código de ética profissional.

00:45:37.000 --> 00:45:54.000
É que é importante ter esse espaço sigiloso, que é, de algum ponto ao outro mais delicado. Assim.

00:45:54.000 --> 00:45:56.000
Certo, uhum.

00:45:56.000 --> 00:45:57.000
Olha só. Deixa.

00:45:57.000 --> 00:46:21.000
Então isso é importante. Mas eu queria outra coisa que eu queria te perguntar, João. Eu tinha entendido isso. Que vai ser possível fazer toda essa reorganização assim dentro do sistema, e aí eu queria te perguntar se a gente vai conseguir antes do treinamento fazer todos esses ajustes antes de começar a treinar.

00:46:21.000 --> 00:46:22.000
Bacana.

00:46:22.000 --> 00:46:27.000
Sim, Sim, com certeza. Sim, até segunda feira, no máximo. Vocês já vão receber os acessos de vocês, tá? O acesso ao ambiente.

00:46:27.000 --> 00:46:29.000
Ah, ok.

00:46:29.000 --> 00:46:33.000
Quando vocês tiverem um tempo livre no expediente de vocês, faz alguns cadastros. O processo já está todo estruturado.

00:46:33.000 --> 00:46:50.000
Então, tem vídeo? Tem manual? Tem tudo. Está dividido em Tóquio, meu Whatsapp está à disposição do Rodrigo também para gente.

00:46:50.000 --> 00:46:51.000
Não.

00:46:51.000 --> 00:47:03.000
Tirando essas dúvidas. E principalmente, para que eu pegue sugestões de vocês. O que a gente construiu aqui é pra gente poder apresentar hoje, nesse primeiro momento, mas está totalmente aberto para que a gente atenda nas necessidades da casamento.

00:47:03.000 --> 00:47:04.000
Não isso. Obrigada, João.

00:47:04.000 --> 00:47:14.000
Beleza por nada. Ele tem mais alguma coisa? Se não tiver conseguindo.

00:47:14.000 --> 00:47:23.000
Tá? Acho que não. Então vamos lá. Esse prontuário que eu mostrei aqui é de uma pessoa que já estava sendo atendida e já foi cadastrada no sistema.

00:47:23.000 --> 00:47:24.000
Tá. E agora, como é que a gente faz quando chega uma pessoa nova? Essa pessoa que agora é uma pessoa nova, que está sendo atendida aqui pela casa.

00:47:24.000 --> 00:47:54.000
Então, no acesso de vocês, que vocês vão receber, vocês vão ter que o canto cadastro, que são os cadastros básicos para você cadastrar o endereço, o interesse que é muito importante, logo a gente vai falar disso para que o da pessoa para poder cadastrar um prontuário de uma pessoa vocês terem um chate onde vocês podem enviar mensagens por dentro do sistema para outros colaboradores ou para outros grupos acompanhamento

00:48:01.000 --> 00:48:08.000
especializado. E todos os psicólogos vão ter acesso. Ou você pode mandar uma mensagem para a Renata.

00:48:08.000 --> 00:48:38.000
Não pode deixar os recados aqui no sistema. Aviso lembrete o que vocês quiserem utilizar da forma que vocês quiserem de acesso a gente disponibiliza dois relatórios, mas o sistema hoje consegue gerar em mato grosso quinze tipos de relatório diferente e a gente gera um relatório para cada pergunta que vocês fazem menos pela série B a gente consegue gerar mais ou menos três cem quinze relatórios diferentes lá

00:48:42.000 --> 00:48:53.000
também. Então, a gente pode vir aqui? Pessoa vai abrir o formulário cru aqui pra gente limpo. Vou colocar aqui que é a pessoa.

00:48:53.000 --> 00:49:03.000
É a pessoa. Apresentação um. Ok, sites. Vou colocar a data de nascimento aleatória.

00:49:03.000 --> 00:49:08.000
Já calcula a idade. Aqui pra gente também. Nome social, em nome da mãe.

00:49:08.000 --> 00:49:19.000
Não é obrigatório. Nacionalidade dessa pessoa é brasileira. Naturalidade de teste, rassou como colocar como parda etnia.

00:49:19.000 --> 00:49:47.000
Também não sou obrigado a declarar. Tem telefone? Um telefone, dois, e mail, não tempos obrigatórios, mas sempre que vocês puderem inserir e ter essa informação das pessoas, eu tenho um plano certeza que vocês sabem que é extremamente importante é reg órgão expedidor e cpf não vou colocar nada a princípio vamos falar um pouquinho de endereço quando eu venho aqui no endereço na minha lupa ele abre para mim essa

00:49:47.000 --> 00:49:56.000
tela de lista de endereços. Pessoal, isso aqui a gente vai batendo no dia a dia e vai pra vocês direitinho, tá?

00:49:56.000 --> 00:50:07.000
O sistema foi construído para que a gente consiga gerar relatórios por região. Tá por região. Então o que acontece?

00:50:07.000 --> 00:50:15.000
Eu moro no avô X. E o Rodrigo mora numa rua ídolo acima da minha. Nós dois temos dois Ceps diferente.

00:50:15.000 --> 00:50:25.000
Mas nós dois somos moradores de taguatinga sul. Qual que é o ideal para o sistema? É que vocês cadastrem o Rodrigo e o João, como taguatinga sul.

00:50:25.000 --> 00:50:55.000
Eu vou mostrar como, mas vocês também podem cadastrar ele. Você pode criar o seu próprio endereço, botar lá o sede da casa do Rodrigo e bota lá da casa do Rodrigo o ideal é que seja feito porque quando a gente for gerar um relatório por endereço vocês vão ver que vocês vão ter lá cem pessoas cadastradas vai ter dez de taguatinga sul com mais quinze de taguatinga sul com mais quinze de

00:50:56.000 --> 00:50:57.000
taguatinga, por exemplo. E essas mulheres não vão ficar unificadas. Vocês depois vão ter que fazer essa contagem.

00:50:57.000 --> 00:51:15.000
Por quê? Porque vários endereços diferentes foram cadastrados para o mesmo lugar. Vocês podem fazer isso, mas não é a melhor prática adotada. Então, o que acontece aqui?

00:51:15.000 --> 00:51:18.000
Qual é o cenário ideal? Chegou uma pessoa, por exemplo, para se abrigar abrigada. E ela é de taguatinga.

00:51:18.000 --> 00:51:31.000
Que é o exemplo que eu estou dando aqui. Agora você vai ter que digitar o nome do laboratório taguatinga, que é o que ele vai buscar na base de dados.

00:51:31.000 --> 00:51:41.000
Qual é o nome da cidade? Brasília, de Brasília. O estado é distrito federal aqui. Dar um entre e ele está pesquisando.

00:51:41.000 --> 00:51:48.000
Em cima. Está processando. Legal. O que ele achou aqui pra gente.

00:51:48.000 --> 00:51:58.000
Ele achou taguatinga. Sempre tá taguatinga norte e taguatinga sul. Todos os séculos são os séculos genéricos.

00:51:58.000 --> 00:52:06.000
O geralzão da região. Tá ok. Tem um salão Baiano aqui que está vindo aqui porque alguém o cadastrou, né?

00:52:06.000 --> 00:52:18.000
Um bairro com o nome de taguatinga usando um certo de Salomão. Tá, então, por exemplo, eu posso pegar aqui taguatinga sempre essa pessoa de lá de taguatinga, centro.

00:52:18.000 --> 00:52:25.000
O número aqui. Ela me deu o apartamento quatrocentos e cinco. E qual que é o ponto interessante? Ah, João, mas pô, eu vou ficar cadastrando a pessoa por região.

00:52:25.000 --> 00:52:54.000
Eu preciso saber aonde que essa pessoa mora. Qual é a rua? O número da casa, na quadra. Se é bairro, se é uma rodovia, se é uma travessia, vocês vão colocar essa informação aqui no complemento do endereço porque quando eu puxar um relatório ali, daquela pessoa o bairro, vai vir em taguatinga sul mas o endereço é o que está no complemento tá então eu e o Rodrigo nós

00:52:54.000 --> 00:53:00.000
moramos em Tabatinga sul. Mas eu moro na quadra quatro, rua dois, casa trinta e cinco.

00:53:00.000 --> 00:53:10.000
A, por exemplo, é o que é importante para você. Enquanto o servidor sabe, essa informação aqui. Tá ok, mas caso contrário você poderia.

00:53:10.000 --> 00:53:26.000
Eu vou limpar essa informação aqui. Então vou tirar isso aqui para dar outro exemplo aqui para vocês. Você poderia cadastrar seu próprio endereço, tá?

00:53:26.000 --> 00:53:56.000
Como assim, cadastrar o seu próprio endereço? Admite, por exemplo, diretoria das unidades rurais. Faz o cadastro de muitas mulheres que moram em assentamento em rodovia, em travessia, que são locais mais isolados, tá então a gente pode vir aqui nesse cone do canto cadastrar Cep você vai colocar o seu endereço tratado eu vou abrir uma Nova tela você vai me dizer qual que é o estado é o

00:53:56.000 --> 00:54:08.000
distrito Federal. Nosso exemplo, que é Distrito federal. Mas você pode cadastrar de todo o Brasil no Distrito Federal. O nome da cidade e o nome do bairro.

00:54:08.000 --> 00:54:38.000
Você pode criar o nome de um bairro. Tá? Qual que é a questão? Se eu venho aqui e coloca um bairro samambaia norte, e o meu coleguinha coloca um bairro samambaia norte, um outro cep porque a gente mora em ruas diferentes ou no fim vai ficar dois registros de dois endereços do mesmo lugar entendeu não é um problema fazendo assim tá mas é que não é o ideal na estação de relatórios vai

00:54:40.000 --> 00:54:57.000
ficar muita informação pra vocês. Eu posso cadastrar aqui o bairro teste seis, o Cep. Não sou obrigado a colocar, porque a gente entende que tem lugar que nem sempre tem.

00:54:57.000 --> 00:55:08.000
Que, por exemplo, como teste. Vai ser dezassete e um, tá? Ele é uma rua. E o meu namorado duro vai ser.

00:55:08.000 --> 00:55:15.000
Também o teste. Só pra mostrar aqui pra vocês.

00:55:15.000 --> 00:55:20.000
Tirar tudo.

00:55:20.000 --> 00:55:40.000
Nome da cidade.

00:55:40.000 --> 00:55:51.000
Se tiver com algum problema aqui, é bom que eu já vou verificar. Mas, como eu disse, é uma profissionalidade que não é o ideal que vocês utilizem eles não estavam deixando o cadastro por algum motivo.

00:55:51.000 --> 00:55:56.000
Eu acho que a permissão desse usuário. Vou verificar depois, mas e o que acontece quando você vem?

00:55:56.000 --> 00:56:01.000
O cadastro é um endereço. Aqui. Você vem. Ele vai dar o que você vai cadastrar?

00:56:01.000 --> 00:56:08.000
O endereço, seja de onde for. E aí, no ato do cadastro desse endereço, aqui, você pode colocar lá o Cep que você cadastrou, tá?

00:56:08.000 --> 00:56:16.000
Ou então você pode vir aqui. E no nosso caso, lá, seria o bairro teste. Que foi o que eu coloquei na cidade de Brasília, o distrito federal.

00:56:16.000 --> 00:56:28.000
Ele ia aparecer aqui. Se assustem. A princípio, sei que passei muita informação, mas vai ser bem tranquilo e a gente vai estar aqui para auxiliar.

00:56:28.000 --> 00:56:53.000
Então eu vou fazer o cadastro dessa pessoa ou região que vocês sempre alteram. Isso estava normal também. Já está bem explicadinho lá no manual. Vou colocar aqui de novo aqui porque ele tirou e o Cep então taguatinga Brasília Distrito federal muito.

00:56:53.000 --> 00:57:03.000
Beleza pegou aqui, tava. Tive Centro quatrocentos e cinco. Tirei aqui o região beleza quadra quatro ou dois, casa treze e cinto.

00:57:03.000 --> 00:57:11.000
A vou dar um. Ok, beleza. Essa pessoa foi cadastrada com sucesso. Vocês viram que já apareceu o botão que de registrar o atendimento, né?

00:57:11.000 --> 00:57:21.000
Que antes não tinha apareceu também todas as obras que eu falei pra vocês, de dependentes de rede de apoio de anexos e de observações.

00:57:21.000 --> 00:57:32.000
Se eu clicar aqui e salvar, ele já vai iniciar um atendimento para essa pessoa. Eu posso pegar aqui copiar o nome dela e fechar. Nada acontece.

00:57:32.000 --> 00:57:41.000
Ela está cadastrada, mas não foi atendido nenhum atendimento foi inserido para ela. Tanto é que o nome dela não está aparecendo.

00:57:41.000 --> 00:57:49.000
Ainda. Se eu vier aqui naqueles mesmos e conizinhos dos bonequinhos aqui.

00:57:49.000 --> 00:58:17.000
Pesquisar o nome dessa pessoa e vem aqui na lupa. Ele abre de novo o prontuário dela para você alterar uma informação ou a pessoa trocou de endereço, trocou o telefone, trocou o e mail tá tudo aqui disponível para você acessar tá registrar atendimento salvar beleza o atendimento já está aqui rodando pessoa a apresentação já está aqui, ó para ser atendida.

00:58:17.000 --> 00:58:31.000
Tá, então eu posso ver aqui no atendimento dela. E novamente, tá lá for um lado dessa pessoa, tá ok, de acordo com aquilo que vocês, que a gente tem dos documentos da casa, abrir.

00:58:31.000 --> 00:58:47.000
Ah, João, eu preciso ter uma evolução administrativa. Preciso ter uma evolução técnica. Além do acolhimento, a gente também precisa botar mais um formulário de outra coisa legal só passar essas informações pra gente que a gente vai seguir aqui vai estar tudo disponível aqui para vocês entendeu?

00:58:47.000 --> 00:59:00.000
Aqui, nessa tela de atendimento. A gente tem essa aba de acompanhante. O acompanhante é a pessoa que está ali com ela que vai ser abrigada com ela ali, naquele momento.

00:59:00.000 --> 00:59:09.000
Na grande maioria dos casos, esmagadora maioria são os filhos. Então olha a diferença que isso daqui é a tela do atendimento pertinente a esse atendimento.

00:59:09.000 --> 00:59:17.000
É o que está acontecendo aqui. No acolhimento. Tá ok. Essa informação aqui.

00:59:17.000 --> 00:59:47.000
Ela não vai para outras pessoas porque é do meu atendimento. É o atendimento que eu estou fazendo agora. Agora, se eu venho aqui no prontuário dessa pessoa e o cadastro que os dependentes dela, todos os dependentes isso daqui é o prontuário isso daqui, é a informação que vai ficar aqui vai acompanhar essa pessoa por todos os lugares que ela passe na secretaria da mulher em todos os equipamentos então isso a gente vai deixando bem claro, para vocês

00:59:49.000 --> 00:59:58.000
no dia a dia, também questão do anexo extremamente importante. Você vai ser um anexo que é pertinente.

00:59:58.000 --> 01:00:08.000
Controle de medicamentos, por exemplo, que é uma informação ali, e outros servidores vão precisar acessar uma informação importante, um anexo que pertence àquela pessoa.

01:00:08.000 --> 01:00:19.000
Uma medida protetiva, um boletim de ocorrência. Os anexos são inseridos aqui no cadastro dessa pessoa, que, no prontuário, tá tem uma grande diferença.

01:00:19.000 --> 01:00:23.000
Eu venho aqui na tela de atendimento.

01:00:23.000 --> 01:00:28.000
Eu sou atiração, barraquinha, ponte.

01:00:28.000 --> 01:00:29.000
Oi.

01:00:29.000 --> 01:00:38.000
João, a Juliana está perguntando se a mulher tiver filhos, mas eles estiverem com alguém da família que não estiverem com ela no abrigo, mesmo assim, cadastramos os dependentes e ela pergunta também filhos maiores.

01:00:38.000 --> 01:00:41.000
De idade entram também em algum registro.

01:00:41.000 --> 01:00:52.000
Sim, essa questão de cadastrar ou não vai do vai. Do que vocês definirem como área de negócio.

01:00:52.000 --> 01:01:01.000
Tá? Existe os locais para se a pessoa tem cinco filhos, você pode cadastrar todos os filhos dela a nível de informação, ação.

01:01:01.000 --> 01:01:02.000
Ah, no momento ela está com três ali. Beleza você pode cadastrar só os três. Ah, ela tem cinco mais dois.

01:01:02.000 --> 01:01:32.000
Somente vão ficar abrigados aqui com ela. E aqui na tela de acompanhante, você cadastra esses dois. Por que João que tem essa tela de acompanhante? Se já tem lá do outro lado, pessoas que você cadastra você também pode manipular elas você pode encaminhar essa criança por uma brinquedoteca por exemplo, entendeu ou para outro setor que faça algum tipo de atendimento especializado para uma criança tá então vamos lá oi.

01:01:37.000 --> 01:01:47.000
João. Isso seria referente àquele critério até pra gente classificar o Cpf. Não é isso de atendimentos pela casa.

01:01:47.000 --> 01:01:48.000
Exatamente exatamente.

01:01:48.000 --> 01:01:54.000
Pra gente contabilizar é para a gente tirar aqueles relatórios, né?

01:01:54.000 --> 01:01:55.000
Entendi.

01:01:55.000 --> 01:02:03.000
Ah, exato. Exatamente. E essa questão que a Juliana perguntou se cadastro ou se não cadastro. Isso é definido pela casa.

01:02:03.000 --> 01:02:16.000
Tá? Mas eu tô querendo deixar bem claro aqui pra vocês a diferença de uma tela de atendimento. Vocês estão vendo que aqui também tem anexo, nada a João. Mas onde é que eu vou?

01:02:16.000 --> 01:02:24.000
Seria o anexo lá da do cepea do Rg dessa pessoa. Por exemplo, aqui não é a tela ideal para isso, porque aqui são anexos.

01:02:24.000 --> 01:02:27.000
Um currículo. Seria aí o currículo.

01:02:27.000 --> 01:02:36.000
Não, também não. Também não. Para ser bem sincero, essa funcionalidade de anexo aqui na tela de atendimento é muito pouco utilizado.

01:02:36.000 --> 01:03:05.000
Por que? Porque o anexo que você insere aqui é pertinente somente a esse atendimento. Então, quando você insere um anexo aqui e encaminha essa pessoa pra outro lugar, esse anexo aqui morre com você essa informação fica com você porque é pertinente, a esse atendimento agora com um currículo que a gente vai precisar consultar que essa informação é extremamente importante que pode surgir proposta de emprego de vaga

01:03:05.000 --> 01:03:12.000
isso tem que estar no prontuário dela. Tem que estar no prontuário dessa pessoa. A pastilha que a gente guarda na gaveta.

01:03:12.000 --> 01:03:21.000
Bom dia. Um milhão de documentos dela. Esse é o controlar, tá? E isso vai ficando mais claro para vocês no dia a dia.

01:03:21.000 --> 01:03:28.000
Só estou deixando bem claro essa informação aqui, tá? Então, beleza. Eu peguei essa pessoa, a apresentação e vamos lá.

01:03:28.000 --> 01:03:34.000
Vou deixar o exemplo aqui pra você. Peguei essa pessoa que a apresentação tá, pesquisei ela aqui e vou cadastrar um dependente pra ela.

01:03:34.000 --> 01:03:47.000
O filho, tá? Esse filho um tem sete anos. Ele está frequentando a escola. Está na sexta série.

01:03:47.000 --> 01:04:00.000
Não sei. Só que esse filho dela mora com os tios, ok? Esse filho dela mora com os tiros beleza, essa informação vai estar disponível para gente sempre, consultar.

01:04:00.000 --> 01:04:13.000
Só que ela também tem outro filho. O filho dois. Tá, esse filho dois tem cinco anos. Ele também está frequente na escola e ele está na segunda série.

01:04:13.000 --> 01:04:22.000
São exemplos. Esse mora com a mãe, por exemplo, com ela, né? Para lá consegue ver que no prontuário dessa pessoa eu tenho dois dependentes cadastrados.

01:04:22.000 --> 01:04:33.000
Essa informação vai estar sempre com ela para todo lugar que ela assume. Ela tem dois dependentes cadastrados.

01:04:33.000 --> 01:04:41.000
Beleza, João, tranquilo. Aí eu posso pegar aqui também. E colocar aqui o termo de entrada que ela assinou da casa.

01:04:41.000 --> 01:04:49.000
Assim. Não tem de entrada aí você vai pegar o termo de entrada que está lá no seu computador pra colocar aqui e vai salvar beleza.

01:04:49.000 --> 01:04:54.000
Esse termo está aqui. Isso aqui vai estar sempre com ela em todo lugar que ela for show. Vamos lá.

01:04:54.000 --> 01:05:10.000
Só que no momento que ela chegou na casa, ela só está com o filho. Dois, por quê? Porque o filho, um mora com um tio e aí, João, o que eu faço nessa situação?

01:05:10.000 --> 01:05:11.000
O filho dois vai ter que ser abrigado ali com ela nesse momento. Então, lá no ato do atendimento dessa pessoa, olha só a diferença.

01:05:11.000 --> 01:05:24.000
Atendimento. Eu estou fazendo o atendimento. Eu vou pegar aqui e cadastrar o filho. Dois dela.

01:05:24.000 --> 01:05:52.000
Que é essa pessoa de sete anos aí? Agora eu faço perguntas sobre o filho dela, por exemplo, se tem alergia se faz uso de medicamento, se tem restrição para que vocês, enquanto os servidores estejam respaldados, caso aconteça algum problema anos, ele não tem alergia não toma nenhum medicamento e não tem nenhuma restrição, alimentar só que ele tem uma observação que é uma criança agitada, salvem

01:05:52.000 --> 01:05:59.000
beleza. Vocês estão vendo que essa criança está aqui no registro? Também haja ou mais, qual a diferença?

01:05:59.000 --> 01:06:05.000
Porque aquele outro lado é o prontuário dela. Aqui. Eu cadastrei. Eu posso interagir.

01:06:05.000 --> 01:06:29.000
Vocês estão vendo que tem dois buraquinhos aqui? Eu posso encaminhar essa criança para uma brinquedoteca, no caso de vocês que não aparece nada, porque a gente não colocou um setor que atende crianças aqui tá, mas se vocês tiverem por exemplo, algum dia chegar até uma casa abrigo mas esse setor, aqui atende criança não só faz isso mas atende também então a gente pode construir aqui dentro para vocês encaminhar

01:06:29.000 --> 01:06:33.000
para quê? Para vocês saberem quantas crianças foram abrigadas. A Idade Média, idade idade se frequenta escola, qual é o percentual de crianças que têm alergia?

01:06:33.000 --> 01:06:50.000
O histórico dessas crianças, para que vocês tenham essa informação, e também se respaldam beleza aqui no atendimento. Eu vim aqui, coloquei as observações.

01:06:50.000 --> 01:06:52.000
O acompanhante? Ela. Vou responder. Que estado civil.

01:06:52.000 --> 01:07:18.000
União estável. Tempo de relacionamento, cinco anos. Os documentos portados. Ela chegou com a certidão de nascimento, certidão de casamento e título eleitoral, número do cartão sus eu vou provar que o número, elatório e possui alergia Sim, possui alergia beleza. Vou salvar esse Formulário.

01:07:18.000 --> 01:07:28.000
Aqui. E aí vou encaminhar ela. Ou então posso finalizar. Por exemplo, vou encaminhar ela para o acompanhamento especializado para fazer a escuta qualificada com o psicólogo.

01:07:28.000 --> 01:07:39.000
Tá, caminhei. Essa pessoa tá lá, beleza. Ela já sumiu daqui, certo? Só que essa pessoa aparece aqui porque ela foi atendida hoje.

01:07:39.000 --> 01:07:47.000
E se eu vier aqui no histórico dela? Eu consigo ver. Opa passou lá acolhimento. Maria atendeu. Ela.

01:07:47.000 --> 01:07:57.000
Então eu vejo que o estado civil dela União estável. Tempo de relacionamento de cinco anos ela estava com certidão de nascimento, casamento, título eleitoral.

01:07:57.000 --> 01:08:01.000
Esse é o número do cartão Sus. E ela tem alergia.

01:08:01.000 --> 01:08:06.000
Entender. Ela agora está no acompanhamento especializado. Vocês vão ver que está vazio. Por quê?

01:08:06.000 --> 01:08:15.000
Porque ela está lá pra ser atendida por alguém, tá? E a questão da evolução técnica que eu sei que existe no caso de vocês, a gente vai construir, tá?

01:08:15.000 --> 01:08:23.000
Então quando você vier aqui para atender uma pessoa, aqui embaixo do acolhimento, vai ter uma evolução técnica.

01:08:23.000 --> 01:08:43.000
Onde você vai? Vai clicar. Vai ser evolução e vai salvar uma hora. A gente precisou levar essa mulher pro hospital porque ela teve um problema e tudo. Mais aí não me interessa quem é o responsável.

01:08:43.000 --> 01:08:52.000
Vocês que vão me dizer se é o agente se é um cuidador, se é um técnico, mas todos vocês vão ter poder para isso.

01:08:52.000 --> 01:08:58.000
Eu posso pegar essa pessoa. Essa Maria. Teste, desligamento voluntário. E posso pegar lá e subir um novo atendimento para ela.

01:08:58.000 --> 01:09:03.000
E inserir uma evolução. Tá ok, tudo isso vai ficando uma piada. Nenhum histórico pra você.

01:09:03.000 --> 01:09:18.000
Consultar durante o período Beleza. Agora que esse meu perfil tem acesso nos dois setores se eu vier aqui nessa casinha vocês estão vendo num ícone superior, eu altero a minha unidade.

01:09:18.000 --> 01:09:33.000
Não é o que vai acontecer com vocês a princípio. Mas eu também tenho acesso aqui. Por exemplo, lá com os psicólogos, então eu creio que agora eu estou vendo o setor do psicólogo, vocês estão vendo que já mudou aqui as pessoas já está diferente.

01:09:33.000 --> 01:09:41.000
Porque os atendimentos aqui são diferentes. É um setor diferente. Então eu estou vendo que a pessoa apresentação está aqui para atender.

01:09:41.000 --> 01:09:48.000
Ela chegou hoje. Dia vinte e nove. Aos cinco. A beleza abro aqui e aqui.

01:09:48.000 --> 01:10:17.000
Eu vou ter o meu acompanhamento especializado. A gente fala de questões um pouco mais íntimas, planejamento familiar, se a gestante, o tempo de gestação aqui, a gente fala da questão da violência propriamente dita de algumas questões sobre o autor aqui medida protetiva e tudo mais tá e qual que é a questão Ah, essa pessoa tá aqui pra atender mas peraí eu não sei nada sobre essa pessoa não tem informação nenhuma o servidor tem

01:10:17.000 --> 01:10:23.000
que chegar aqui me passaram a documentação. Não precisa. Você pode vir aqui no histórico. Poupa beleza.

01:10:23.000 --> 01:10:28.000
Deixa eu ver. A Maria atendeu. Ela você tem acesso a essas informações, tá? Se?

01:10:28.000 --> 01:10:42.000
Arras, espera e deixa eu ver. Eu preciso pegar o número do Rg dessa pessoa. E eu preciso ter também o acesso à certidão de nascimento dela, mesmo.

01:10:42.000 --> 01:10:51.000
Pesquisa que está aqui, o endereço, a nacionalidade. A gente não preencheu, aí o que acontece aquele independente que eu cadastrei?

01:10:51.000 --> 01:11:00.000
O filho dois. Ele foi cadastrado lá no acolhimento e foi encaminhado. Acabou. Mas se eu vier no prontuário dessa pessoa.

01:11:00.000 --> 01:11:02.000
Olha ele aqui. Por quê? Porque outra pessoa já cadastrou previamente. Então, essa informação dos filhos dos dependentes.

01:11:02.000 --> 01:11:18.000
Eles vão acompanhar. Pessoas. Sentem todo em qualquer setor. A pessoa tem dois filhos.

01:11:18.000 --> 01:11:25.000
A rede de contato dela, que estaria aqui também. Gente não cadastrou. Mas eu posso pegar e cadastrar a Maria, que é amiga.

01:11:25.000 --> 01:11:33.000
Telefone, tal tal. Tá lá ou para algum tipo de problema? Eu posso entrar em contato com essa marinha, que é uma amiga dela, tá?

01:11:33.000 --> 01:11:42.000
Os anexos Olá, o termo de entrada que a gente que a gente inseriu tá, então aqui vai ficar tudo sobre essa pessoa.

01:11:42.000 --> 01:11:45.000
Se documentos iniciais. Essa carga de documentação tá? E eu estou em outro setor. Já estou no acompanhamento especializado.

01:11:45.000 --> 01:12:01.000
Então é um servidor que está trabalhando em Santa Maria, por exemplo. Vamos supor. Se fosse assim servidor que está trabalhando em Santa Maria, preenche essa informação e eu tô lá no Gama aqui, trabalhando aqui em conjunto com essa pessoa, tá?

01:12:01.000 --> 01:12:11.000
Posso encaminhá la de volta para o acolhimento também, caso seja necessário. Tá, então é completamente flexível esse fluxo e o que vocês precisam?

01:12:11.000 --> 01:12:22.000
Eu acho que essa parte aqui, inicialmente, de estar clara por audiência, muita informação. Não precisam se preocupar.

01:12:22.000 --> 01:12:33.000
E tudo isso vai ser explicado e a gente vai estar à disposição. Eu vou mostrar para vocês. É só a cara do nosso servidor de produção que está oficial.

01:12:33.000 --> 01:12:41.000
Lá só vão ter nomes. Não tem nenhum tipo de dado sensível. A gente não vai apresentar nenhum tipo de dado sensível para vocês.

01:12:41.000 --> 01:12:50.000
Ok? Só para que vocês tenham mais ou menos uma noção do volume de atendimentos e do que a gente pode fazer nos relatórios.

01:12:50.000 --> 01:12:57.000
Vou acessar aqui. Rapidinho. Esse daqui é o nosso servidor oficial, que é o que o pessoal utiliza.

01:12:57.000 --> 01:13:05.000
Eu tenho um perfil específico pra isso. Nesse perfil aqui, eu não consigo interagir com nenhum dado, mas eu consigo ver todos os relatórios.

01:13:05.000 --> 01:13:13.000
Ok, então aqui a gente consegue ver aqui no canto que a gente tem hoje. Dois mil, quatro, cem, dois mil, cinto, cem, catorze e sete atendimentos.

01:13:13.000 --> 01:13:25.000
Esses atendimentos são reais. Esses dados são reais. Você consegue ver aqui hoje, quatro pessoas passaram pela casa, tá? Foram e estão sendo atendidas.

01:13:25.000 --> 01:13:55.000
Ontem foram mais sete. Não te ontem foram mais oito. E aqui, assim por diante. Então é mais ou menos esse volume das informações aqui a gente tem dois, cem quinze e cinto, páginas de pessoas que estão sendo atendidas e foram encaminhadas que já foram finalizadas e é mais ou menos essas telas que vocês vão ver também só que a diferença é agora todo o sistema se comunica então a casa abriu vai se comunicar diretamente com a casa,

01:14:00.000 --> 01:14:10.000
da Mulher Brasileira. E futuramente, os outros equipamentos também protegendo o sigilo e a confidencialidade de cada um dos setores.

01:14:10.000 --> 01:14:14.000
No relatório. Por exemplo, a gente tem um relatório aqui de pessoas.

01:14:14.000 --> 01:14:17.000
A vidas.

01:14:17.000 --> 01:14:20.000
Alguém falou?

01:14:20.000 --> 01:14:26.000
Aproveitando João. A Luciane está perguntando se mais de uma pessoa pode ter acesso ao prontuário ao mesmo tempo.

01:14:26.000 --> 01:14:27.000
Pode. Pode sim.

01:14:27.000 --> 01:14:33.000
Tem espaço específico para registrar contato da rede de apoio dela, tanto primária quanto a institucional.

01:14:33.000 --> 01:14:40.000
Tem que é naquele campo que eu mostrei de contatos naquela barra de contatos. Lá já é fixo.

01:14:40.000 --> 01:15:06.000
Mas não formulário. A gente já colocou também um local para vocês cadastrarem a rede de apoio, porque eu vi que vocês utilizam no prontuário do que já tem forem suficientes, e insuficientes vocês têm lá no formulário também no local que você pode colocar isso eu acho que até me lembro o local que trabalha essas informações institucionais.

01:15:06.000 --> 01:15:12.000
Do formulário. Tem mais alguma pergunta?

01:15:12.000 --> 01:15:13.000
Tá. Não.

01:15:13.000 --> 01:15:17.000
Não pode continuar. Tem uma no final da Maira. Dá uma sugestão e a Cláudia. Mas a gente conversa no final sobre isso.

01:15:17.000 --> 01:15:23.000
Beleza. E aí, pessoal? Eu tô mostrando isso aqui porque a gente não teria um dado sensível.

01:15:23.000 --> 01:15:30.000
Aqui, tá? A gente não vai abrir nenhum relatório. Nenhum prontuário nem nada. Aqui está.

01:15:30.000 --> 01:15:38.000
Quando vocês tiverem entre assinarem os termos de compromisso, vocês vão poder consultar aquilo que não é sigiloso.

01:15:38.000 --> 01:16:08.000
Tá? O que é sigiloso? Já está resguardado aqui. As pessoas que estão cadastradas vou colocar aqui para que vocês tenham noção da quantidade então vou pegar uma data bem grande, dois mil, dezanove para cá a gente pode ver por exemplo, por idade, então a gente consegue ter um percentual legal aqui gente hoje tem sete cem treze e oito pessoas cadastradas Luiz desde quando a gente implementou até hoje e aqui a gente tem as quantidades de acordo com o percentual

01:16:12.000 --> 01:16:42.000
de idade majoritariamente entre catorze e um a quinze anos de idade, a gente só teve somente duas pessoas maiores de dezoito anos, por exemplo, como esses são dados quantitativos, não qualitativos, a gente pode ver que eu posso mostrar para vocês porque não fere a confidencialidade do dado sensível de ninguém só para vocês, terem ideia mais ou menos do que o sistema pode fazer bem legal também para você ter essa visualização

01:16:45.000 --> 01:16:54.000
mais facilitada das idades. Por exemplo, a gente consegue ter para o bairro. Essa aqui é a questão dos bairros que eu falei.

01:16:54.000 --> 01:17:22.000
Olha só. Tanto de bairro que a gente tem cadastrado hoje aqui quarenta e seis e o pessoal não no cadastro no bairro, nem muito, mas a gente consegue rastrear pelo nome do endereço que, por exemplo, estão vendo acampamento Nova Jerusalém sampaio uma acampamento Nova Jerusalém e samambaia estradas de formas diferentes do mesmo endereço tá e aqui a gente pode gerar um

01:17:22.000 --> 01:17:32.000
relatório para vocês normal no caso que é da casa da mulher brasileira. E aí vocês fazem uma filtragem. Vocês vão saber quantas pessoas têm do acampamento.

01:17:32.000 --> 01:17:37.000
Nova Jerusalém, por exemplo. Mas não fica facilitado. Não fica da forma que é o ideal a se funcionar.

01:17:37.000 --> 01:17:46.000
Então, aqui a gente tem essa série de bairros cadastrados no núcleo rural, planaltina, riacho, fundo Samambaia.

01:17:46.000 --> 01:17:49.000
Lembrando que aqui não tem o endereço de ninguém.

01:17:49.000 --> 01:17:59.000
E dar essas setecentos e trinta e oito por bairro por região com raça. Também eu vi. Era o mesmo relatório.

01:17:59.000 --> 01:18:27.000
Outro tipo de relatório aqui são os de atendimentos de pessoas atendidas por data o que é interessante nesse relatório, que, além de gerar um dado quantitativo de mulheres de Cpfs de prontuários únicos, ele tiver também o mapeamento por onde aquela pessoa, passou então eu vou parar aqui, de um período curto para não ficar tão grande um relatório, obrigado desse mês, por exemplo, a gente consegue ver aqui por exemplo, que no dia primeiroo de Maio, de dois mil vinte

01:18:27.000 --> 01:18:53.000
e quatro. A gente teve essa pessoa que passou pelo alojamento, tá? O status ficou finalizado durou somente sete segundos, porque provavelmente o servidor só inseriu os dados dela e já finalizou e a gente teve essa outra pessoa no dia, primeiro de Maio, quando as pessoas a gente teve duas tá é contado que é o o prontuário aqui a gente faz todo o mapeamento também ao final desse

01:18:53.000 --> 01:19:05.000
dia que no dia dois, cinco pessoas. E tem todo um mapeamento. Se essa pessoa que foi encaminhada para casa, para casa, abrigo, o acompanhamento encaminhou lá para casa abrir.

01:19:05.000 --> 01:19:11.000
Ela vai aparecer aqui também. Tá? Então a gente não faz a contagem mais de uma vez da mesma pessoa.

01:19:11.000 --> 01:19:20.000
Essa pessoa é mapeada. Os atendimentos são contados e o fluxo dela é acompanhado de ponta a ponta até o fim.

01:19:20.000 --> 01:19:27.000
Então ele vai aparecendo aqui conforme ele é atendido. Aqui, a gente tem uma série de outras páginas.

01:19:27.000 --> 01:19:57.000
Qual que é a vantagem? Esse relatório aqui, ele gera um relatório geral de todo mundo que está dentro da secretaria da mulher, ou seja, fica difícil para vocês na ponta separar o que é da casa abrigo pensando nisso, a gente já desenvolveu uma outra ferramenta que vai ser oficializado, bem simplesmente pois bem simples para que vocês tenham exatamente a contagem de prontuários e a contagem de atendimentos mulheres

01:20:00.000 --> 01:20:18.000
atendidas de atendimentos, tudo isso. Então, com dois, três cliques, vocês vão conseguir ter essa informação individualizada, seja por setor, ou seja, na casa amigo inteira.

01:20:18.000 --> 01:20:25.000
Isso tudo vai ser passado por vocês. Para vocês, beleza, estou aqui só para mostrar essa questão dos relatórios.

01:20:25.000 --> 01:20:52.000
Beleza. Esse aqui é mais um dos tipos de relatório que a gente pode gerar. Eu tenho aqui o gráfico de quantidade de atendimento por setor interessante, porque o que eu posso selecionar aqui, por exemplo, admite que a unidade rural por exemplo, eles têm só uma categoria que é da sub Pm e aqui são os itens que item são esses jovens tudo aquilo que eles podem de informação lá e é por isso que eu falei que a gente.

01:20:52.000 --> 01:21:01.000
Consegue gerar muito o relatório porque para cada informação que vocês coletam, a gente gera um relatório que eles fazem um questionamento lá.

01:21:01.000 --> 01:21:31.000
De qual a sua ocupação tá na de muro. Selecionar esse item vou botar numa data bem grande, eu não lembro quando que eles começaram a utilizar e vou selecionar aqui, o setor então a gente consegue ver que de dois cem dezasseis e nove mulheres que responderam tá como majoritariamente catorze virgula, cinto declarou que está desempregado então a gente consegue gerar essa informação aqui de tudo aquilo

01:21:33.000 --> 01:21:46.000
que você coleta lembrando o íris. Trabalha com dados quantitativos, quantidade. A gente já está trabalhando aqui em parceria com a gestão estratégica para entregar para vocês os dados qualitativos.

01:21:46.000 --> 01:21:55.000
Ah, ela declarou que tem interesse na área jurídica. Beleza quando surgia alguma parceria, algum projeto, oportunidade de emprego, de área jurídica.

01:21:55.000 --> 01:22:07.000
A gente consegue dizer quem são essas pessoas. Lógico que, com todo o sigilo do mundo, um acordo alinhado com a área estratégica, então facilita para todas as pontas.

01:22:07.000 --> 01:22:13.000
Aqui, o mesmo gráfico que eu mostrei para vocês. E isso ele gera todos os itens que a gente tem aqui dentro.

01:22:13.000 --> 01:22:43.000
Por exemplo, estado civil, né? Então a grande maioria é casada com união estável, e a gente consegue ter esses dados de tudo aquilo que a gente coleta, passando para o próximo aqui, agora que são os gerenciais a gente tem o perfil dos funcionários não interessa ainda para vocês porque vocês não estão cadastrados aqui, mas assim que tiverem, vamos conseguir ver o que cada um tem de perfil quantidade de pessoas atendidas por setor eu posso pegar por exemplo,

01:22:47.000 --> 01:22:56.000
admuo de novo como um exemplo, não uma data bem grande. Hoje, meu primeiro esse relatório aqui.

01:22:56.000 --> 01:23:24.000
A gente consegue ver nesse cara. Aqui. Tudo o que foi a quantidade de respostas que a gente teve para cada pergunta e as quantidades, você consegue ver que, por exemplo, a gente tem a primeira pergunta: que gênero, então a gente tem quatro opções e as quantidades do total esse relatório que é interessante, porque ele dá pra gente também é a quantidade, de pessoas cadastradas estão aqui é obrigatório todo mundo que passa por ela tem que responder

01:23:24.000 --> 01:23:32.000
automaticamente. Eu tenho a quantidade de mulheres que foram atendidas pela admiração, entende? Então, nesse caso, aqui a gente tem essa média.

01:23:32.000 --> 01:23:46.000
Dois, cem, quinze, dois, cem, vinte, dois, cem, treze, cem, catorze. Mas tem uma questão aqui: que tem mais de quatro, cem, dezanove respostas, pelo menos quatro, cem, dezanove mulheres foram cadastradas e atendidas pela tutela de mur.

01:23:46.000 --> 01:23:50.000
Nesse período, entendeu aqui, por exemplo.

01:23:50.000 --> 01:23:58.000
Se tem interesse em alguns dos testes rápidos. Abaixo Leicia! Hepatite Hiv e simples cinto.

01:23:58.000 --> 01:24:04.000
Cem, catorze respostas, que é exatamente o número de mulheres que foram cadastradas pela de muro nesse período.

01:24:04.000 --> 01:24:13.000
Então esse aqui é um relatório geral. Pra que vocês possam ter uma visão geral de quantidades, e tudo aquilo que é respondido na casa.

01:24:13.000 --> 01:24:43.000
Abril, passando rapidinho. Aqui também aqui, os Estados das pessoas mostram as quantidades quantas, atendendo quantas, para atender, quantas encaminhadas são os atendimentos por bairro, eu posso passar o nome da pessoa Washington vou pegar todos os Bairros e o nome aqui eu vou pegar não esse aqui é o ambiente oficial eu pegar aqui, dois mil e dezanove recuperar uma pessoa aleatória, que talvez nem tenha porque não vai ter

01:24:53.000 --> 01:25:01.000
porque não teve atendimento para nesse período. Mas eu vou. Vou enfrentar alguns dos dados de homologação e depois mando pra vocês também.

01:25:01.000 --> 01:25:02.000
É que ele gera todos os atendimentos que essa pessoa específica teve, ou todos os atendimentos que aquele bairro específico teve, facilita também essa gestão.

01:25:02.000 --> 01:25:21.000
Aqui o relatório de tempo de atendimento, tá? Então a gente tem aqui, por exemplo, vou pegar desse mês a data final.

01:25:21.000 --> 01:25:35.000
Setor. Vou botar um exemplo. E vou trazer aqui todo mundo é que a gente tem as datas dos tempos dos relatórios de atendimento.

01:25:35.000 --> 01:25:41.000
Por exemplo, nesse mês. Por enquanto, a de muro só fez esses três atendimentos porque eles já cadastraram muitas pessoas.

01:25:41.000 --> 01:25:49.000
Então, aqui a gente tem mais ou menos a hora de entrada. Hora de saída. O status e essas outras informações aqui tá.

01:25:49.000 --> 01:25:54.000
Se eu pegar de outro setor aqui, por exemplo, vocês vão ver que é bem maior.

01:25:54.000 --> 01:26:22.000
Então esse aqui é do acolhimento. Por exemplo, a origem, o destino, o status na hora de entrada, a hora de saída, o tempo que essa pessoa passou então vocês conseguem ver que lá no acolhimento que foi encaminhado para o acompanhamento essa pessoa que ficou catorze dias sendo atendida então será que já existe hoje na casa da mulher brasileira também consegue mapear todas as informações aqui eu tenho um prontuário

01:26:22.000 --> 01:26:28.000
dessa pessoa. O número de atendimento. Gente consegue mapear essa informação, tá?

01:26:28.000 --> 01:26:58.000
E aqui eu tenho um relatório de produtividade de atendimento por período. É um relatório que não sei se era muito bem visto por todos, mas a gente consegue mapear também a produtividade de cada servidor, por período que a gente tem as pessoas a quantidade de atendimentos no total no setor aqui a gente tem outro setor também porque a gente tem outro setor também e a gente consegue fazer esse mapeamento em um período tá ok, todos esses relatórios vão estar disponíveis no

01:27:03.000 --> 01:27:13.000
perfil de consulta para vocês vai ser liberado também. A ferramenta para vocês poder distrair a quantidade de pessoas atendidas e de atendimento também.

01:27:13.000 --> 01:27:20.000
Tudo isso vai ser oficializado pelo sei, vocês vão ter suporte e respaldo o tempo todo. Tá ok.

01:27:20.000 --> 01:27:25.000
Treinamento. A gente já tem as datas a gente vai conversando sobre isso. Os manuais também já têm segunda feira.

01:27:25.000 --> 01:27:34.000
Vocês já vão estar com o acesso. Cada um com o seu assassino liberado, tá? E vai ter uma nota.

01:27:34.000 --> 01:27:42.000
Mente como vocês alteram esse sangue. Qualquer dúvida, qualquer problema, eu vou estar à disposição. E o Whatsapp do Rodrigo também.

01:27:42.000 --> 01:27:52.000
Ele vai direcionando para não beleza. Rodrigo, você consegue ver se tem mais alguma dúvida pendente? Se tem?

01:27:52.000 --> 01:28:01.000
João. A Andreia pergunta para o relatório: é possível selecionar mais de uma categoria de dados e ela pergunta também se podemos acrescentar categorias.

01:28:01.000 --> 01:28:12.000
Pode sim. Vamos lá responder na primeira pergunta, André deixou só voltar ali naquele relatório de categoria, que é o que você escolhe no formar.

01:28:12.000 --> 01:28:14.000
Vocês só podem colher um ano, tá? Vocês socorrem um ano. Mas tem aquele outro relatório que eu te mostrei.

01:28:14.000 --> 01:28:30.000
Aqui te dá a quantidade de tudo. Tá ok, então vamos lá. Qual que é a diferença? Quantidade de pessoas atendidas, gráfico de quantidade de atendimentos por setor.

01:28:30.000 --> 01:28:58.000
Eu venho aqui. Coloquei aqui. Seleciona que é a categoria e o item. Está vendo que são todas as perguntas aqui, eu só posso selecionar um por um, e ele me dá as quantidades e valores tá que foi aquele que eu mostrei mas se a gente vier aqui no quantidade de pessoas atendidas por setor eu posso selecionar o setor então no caso de vocês lá vai ser por exemplo, a acompanhamento

01:28:58.000 --> 01:29:09.000
especializado. Você seleciona a data, o período, e eu vou te entregar aqui. Um relatório geral de todas as categorias, tá, então podemos. Sua pergunta?

01:29:09.000 --> 01:29:20.000
Aquele relatório específico só traz não, mas esse relatório aqui traz tudo sobre a questão das novas categorias.

01:29:20.000 --> 01:29:28.000
A gente vai construir.

01:29:28.000 --> 01:29:58.000
Vamos lá. Outra pergunta aqui. Eu deixei pro final pra gente conversar. Respeito e a gente pode até, como o João disse, a gente vai ter um período que vocês vão fazer os testes no ambiente de testes para dar o feedback do que precisa melhorar às vezes, algum algum campo está incompleto então o que aconteceu a gente conversou com maíra mayra cândido que fez esse levantamento de requisitos pra

01:30:00.000 --> 01:30:08.000
gente. A gente conseguiu inserir alguns formulários no Iris. E agora vocês precisam testar pra falar.

01:30:08.000 --> 01:30:22.000
O que que precisa tirar. O que precisa acrescentar aí a maíra pergunta aqui João. E aí, junto com a pergunta da Cláudia, a pergunta não a afirmação da Cláudia.

01:30:22.000 --> 01:30:32.000
Duas afirmações. A Claudia fala. Tem que haver três níveis: um de acolhimento, um pra especialistas em geral e um só pra psicólogo.

01:30:32.000 --> 01:30:38.000
A Maira já fala. Será necessário criar o mesmo sigilo ao assistente social, conforme prevê o nosso código de ética.

01:30:38.000 --> 01:30:47.000
Eu queria maira que você me informasse um pouquinho mais sobre isso. Tem essa necessidade mesmo de Itu.

01:30:47.000 --> 01:30:54.000
Assistente social ter um. Um sigilo só para ele igual. Os especialistas vão ter.

01:30:54.000 --> 01:30:57.000
Oi, pessoal. Boa tarde. Tudo bem então, Rodrigo.

01:30:57.000 --> 01:30:58.000
Boa tarde.

01:30:58.000 --> 01:30:59.000
Boa tarde.

01:30:59.000 --> 01:31:27.000
É assim como o código de ética do psicólogo. A gente também tem essa responsabilidade. Enquanto assistente social, ocorre que são informações que muito raramente a gente não compartilha, considerando que é uma equipe interdisciplinar, né então assim é um outro caso que já passou por mim, que eu tive que lacrar, em prontuário, físico a informação em envelope para que apenas um assistente

01:31:27.000 --> 01:31:28.000
social possa acessar, que eu acredito que vai ser a mesma demanda do psicólogo, né? Existe algumas informações que o usuário.

01:31:28.000 --> 01:31:55.000
Ele pede que seja confidencial e que a gente não pode abrir para uma equipe toda. E muito raro. Pelo código de ética, a gente teria que ter também algumas informações registradas em sigilo para um assistente social poder abrir.

01:31:55.000 --> 01:31:56.000
Beleza, beleza.

01:31:56.000 --> 01:32:02.000
E. E aí, João? O que a gente pode conversar a respeito depois, quanto a isso?

01:32:02.000 --> 01:32:14.000
Tranquilo é essas questões. Então vocês vão começar a utilizar agora, na prática, e vão perceber a falta de setores ou falta de perfis.

01:32:14.000 --> 01:32:21.000
Tudo isso que for necessário. A gente precisa de acolhimento, acompanhamento especializado e psicólogo. Beleza.

01:32:21.000 --> 01:32:28.000
A gente vai criar. Ah, gente precisa que o psicólogo tenha o sigilo. A gente vai criar aí.

01:32:28.000 --> 01:32:53.000
Eu preciso que vocês me passem também. Qual é o formulário que vai ser utilizado? Se é diferente ou do psicólogo por um assistente social, o que é sigiloso e o que não é se tudo é sigiloso, ou não é esses pontos são completamente flexíveis, então eu acho que vocês podem passar essa questão para renata podem alinhar essa questão com a renata e aí a gente vai chegando no

01:32:53.000 --> 01:33:10.000
escopo ideal, mas eu acho que vocês vão conseguir transcer um discernimento melhor quando vocês estiverem utilizando o sistema na prática. Mas só para tranquilizar tanto o que a maíra falou quanto ela falou é completamente possível de ser construído.

01:33:10.000 --> 01:33:18.000
Quando a mulher está acolhida na casa, abrigo. Outras unidades já tem acesso? É uma pergunta da Renata.

01:33:18.000 --> 01:33:19.000
Hum.

01:33:19.000 --> 01:33:24.000
Quando ela está acolhida, o que não é sigiloso. Sim.

01:33:24.000 --> 01:33:25.000
Ok.

01:33:25.000 --> 01:33:29.000
Então, por exemplo, a Renata, a mulher, foi cadastrada ali.

01:33:29.000 --> 01:33:30.000
Oi.

01:33:30.000 --> 01:33:38.000
E que a casa Abriga é sigilosa, né, João é que a Casa abrigo já é por si sigilosa.

01:33:38.000 --> 01:33:39.000
Hum.

01:33:39.000 --> 01:33:44.000
Exatamente esse cenário que a gente vai ter que construir, entendeu? Por exemplo, a casa abrigo hoje realiza um encaminhamento pra casa da mulher brasileira.

01:33:44.000 --> 01:33:45.000
Ou ao contrário.

01:33:45.000 --> 01:33:49.000
Porque essa contra referência que essa contra referência a gente não faz, né?

01:33:49.000 --> 01:33:56.000
Tá? Ela não volta pra casa da mulher brasileira.

01:33:56.000 --> 01:33:57.000
Vozes livres.

01:33:57.000 --> 01:33:58.000
Entendi.

01:33:58.000 --> 01:34:07.000
Ela volta após desligamento. João, a gente faz encaminhamento. Se ficar bom para ela continuar esse acompanhamento na série B de, né?

01:34:07.000 --> 01:34:08.000
Beleza, beleza.

01:34:08.000 --> 01:34:20.000
Eu acho que essa pergunta da Renata. Ela é pertinente porque, pelo sigilo, o ideal que as informações que a mulher está na casa talvez não fique aberto assim.

01:34:20.000 --> 01:34:28.000
Talvez outros equipamentos. Seria nisso que a Renata pensou. Foi Renata.

01:34:28.000 --> 01:34:38.000
Aí uma dúvida. Quando essa pessoa é desligada da casa abrigo e vocês fazem um encaminhamento pra um equipamento externo.

01:34:38.000 --> 01:34:47.000
O equipamento externo tem acesso a um formulário que foi preenchido. Não estou falando que ele precisa ter acesso aos documentos dessa pessoa.

01:34:47.000 --> 01:34:48.000
O formar do acompanhamento, para saber se essa pessoa é gestante. Se fumo, se gere bebida alcoólica ou algo do tipo.

01:34:48.000 --> 01:35:04.000
Os outros equipamentos chegam a ter esse acesso ou que construído dentro da casamento. Só fica na casa. Mim.

01:35:04.000 --> 01:35:05.000
Oi, João. Isso hoje já foi tratado. Está em reuniões. A gente perde.

01:35:05.000 --> 01:35:19.000
Sim, os equipamentos. Tem a necessidade de receber essas informações pra que os especialistas não precisem fazer essa outra avaliação.

01:35:19.000 --> 01:35:20.000
Entendi.

01:35:20.000 --> 01:35:23.000
Já tem a Secretaria da Mulher. Não tem necessidade de chegar no equipamento e ter esse fazer novamente essas perguntas.

01:35:23.000 --> 01:35:31.000
Qualquer informação que ficar na casa, abrigo. E ela foi encaminhada para o equipamento. Deve ir junto.

01:35:31.000 --> 01:35:35.000
Entendi porque assim o pessoal é o seguinte: o sistema é utilizar um sistema.

01:35:35.000 --> 01:35:39.000
Até porque lá essa mulher vai ter. Vai ser assistida também por psicólogos, né? Então é mesmo?

01:35:39.000 --> 01:36:09.000
Sim, o sistema íris é um sistema que é altamente interno. Somente equipamentos hoje, no caso, só a casa da mulher brasileira, somente servidores que tem suas especialidades ali, que tem o seu código de ética e tudo mais somente essas pessoas acessam o sistema para que ninguém veja nada da casa, abrigo, todos os setores da casa abrigo devem estar com tudo sigiloso tá o que é que eu falo que pode ser visto

01:36:11.000 --> 01:36:36.000
por outros setores. São essas informações de acolhimento. São essas informações. Se a pessoa faz uso de bebida alcoólica, se ela é fumante, se ela tem um ou dois ou três filhos, aquilo que for do escopo da casa abrigo e eu já entendi que tudo é sigiloso gente está dentro de um órgão público aqui que trata de uma pauta extremamente sensível tudo é sigiloso, mas eu estou falando.

01:36:36.000 --> 01:36:48.000
De informações que rodam dentro de um sistema interno dentro de equipamentos que são internos. Aquelas informações ali pertinente ao acolhimento.

01:36:48.000 --> 01:37:02.000
Ele não foi construído no escopo inicial para ser sigiloso entre os equipamentos, que for sigiloso, é definido por vocês o que é o sigiloso é aquilo que só o setor pode ver somente o setor pode ver eu já entendi que todo o prontuário vai ser sigiloso.

01:37:02.000 --> 01:37:32.000
Mas esse sigilo já está respaldado pelo fato de ser utilizado. Sistema interno com pessoas que assinam termo de compromisso e que eu, através do banco de dados, consigo ver toda e qualquer tipo de alteração ou manipulação de dados inadequados então a gente está dentro de um ambiente controlado interessante deixar isso bastante claro, mas se a casa, abrigo definir que há somente servidores da casa branca vamos ver

01:37:36.000 --> 01:37:45.000
essas informações aqui, além do que já é sigiloso, que já tá previsto ser construído. Aí tudo de vocês não tem que ficar assim de novo. Só que.

01:37:45.000 --> 01:37:55.000
Qual é a questão quando essa pessoa foi encaminhada para outro local, ninguém mais ver essa informação morre com vocês.

01:37:55.000 --> 01:37:56.000
Eu.

01:37:56.000 --> 01:37:57.000
Aí dentro a princípio. Então é bom a gente construir cenários e testando.

01:37:57.000 --> 01:38:08.000
E teria como fazer uma migração depois, João, tipo assim, durante a permanência na casa, ficaria tudo sigiloso depois do desligamento, isso se tornar compartilhado para os equipamentos, pelo menos o que a gente achar que era possível.

01:38:08.000 --> 01:38:17.000
Não, esse cenário hoje não existe. Dentro do íris. Mas eu já entendi a demanda e a preocupação.

01:38:17.000 --> 01:38:24.000
São coisas que ao final aqui, eu vou conversar com o Rodrigo também. A gente vai alinhar. A princípio.

01:38:24.000 --> 01:38:51.000
Esse formato não existe, tá? Eu consigo definir o que. É o que não é sigiloso. De acordo com o que vocês me passaram, mas não é viável ficar alterando uma hora sigiloso e quando ela sair, não é uma hora é outra hora não é esse escopo tem que ser definido então seria algo que a gestão vai ter que participar, desse daí pra gente chegar num consenso, mas se tiver que ser tudo

01:38:51.000 --> 01:38:54.000
sigiloso. Também é possível. Dá para a gente construir. Eu.

01:38:54.000 --> 01:39:02.000
João e a Cláudia pergunta: E quando a mulher é atendida pelos especialistas os filhos estão sendo acompanhados.

01:39:02.000 --> 01:39:06.000
Os cuidadores. Tem como ter esses dois atendimentos.

01:39:06.000 --> 01:39:19.000
Até aí. Nesse caso, o que a gente pode fazer? Ou a gente pode construir um setor específico pro cuidador onde ele vai armazenar os dados dessas crianças.

01:39:19.000 --> 01:39:48.000
Eles, ou a gente pode criar um cango a mais ali. Para que vocês ensinam essa informação? Ah, se a pessoa tiver dependentes, informe por quem estão sendo atendidos, você vai informar isso é algo que é possível de construir também que vocês vão perceber na prática, se for necessidade se for preciso que a gente construiu a gente vai construir conforme vocês pedirem.

01:39:48.000 --> 01:39:56.000
Ok, vamos a mais perguntas, pessoal.

01:39:56.000 --> 01:40:08.000
Alguns atendimentos são feitos ao mesmo tempo por mais de um especialista. Nesse caso, esse atendimento tem como entrar a ambas as matrículas dos servidores.

01:40:08.000 --> 01:40:16.000
Para constar que foi um atendimento coletivo no caso, em conjunto, pelos especialistas.

01:40:16.000 --> 01:40:27.000
Hum, que acontece? É o seguinte: vários especialistas, independentemente da especialidade, podem atender a mesma pessoa no mesmo período de tempo.

01:40:27.000 --> 01:40:33.000
A questão é que, para que isso aconteça, vai ter a pessoa ali, para mim. Eu vou lá. Seria o atendimento.

01:40:33.000 --> 01:40:42.000
Ah, fez a evolução técnica. E aí, quando eu fizer esse trâmite e salvar, aí sim, a Juliana pode pegar essa pessoa lá.

01:40:42.000 --> 01:40:46.000
Se a gente estiver no mesmo setor e inserir outro atendimento para ela, mas sem concomitante junto.

01:40:46.000 --> 01:40:56.000
Para que fique. Essa pessoa foi atendida pelo servidor. Matrícula, tal tal tal tal tal sistema.

01:40:56.000 --> 01:41:05.000
Mas o que vai acontecer é o seguinte: vai estar lá no histórico da Juliana que ela foi atendida pelo Rodrigo, que foi atendida pelo João foi atendida pela maíra.

01:41:05.000 --> 01:41:29.000
Foi atendida pela Valéria e vai, tá lá. As evoluções de cada um. As informações que cada um preencher, às vezes, por exemplo, o que compete à violência, eu, o que compete aos dados do alto Rodrigo, em série isso é possível por exemplo, cada um ministério sua parte cada um faz sua evolução não sei e aí isso vai estar no histórico dela vai estar ali a matrícula de todo mundo mas

01:41:29.000 --> 01:41:35.000
dentro do mesmo atendimento ali. Não é possível.

01:41:35.000 --> 01:41:46.000
João. A Cláudia perguntou se tem campo pra atividades em grupo e se. E fala que tem grupos que são realizados por três especialistas ao mesmo tempo.

01:41:46.000 --> 01:42:14.000
Ok, é isso que eu acabei de falar. Se a questão do atendimento. No momento, ele pertence a somente em uma pessoa, apesar de que vários atendimentos e várias evoluções podem ser inseridas se a gente precisa colocar alguma informação específica Ah, se é um atendimento em grupo quem são as pessoas, aí a gente pode criar isso lá dentro, mas atribuir ou dizer que três pessoas fizeram um atendimento ao mesmo tempo, hoje não existe dentro do

01:42:14.000 --> 01:42:16.000
sistema.

01:42:16.000 --> 01:42:22.000
Tem outra pergunta? Juliana, tá com a mão levantada aí.

01:42:22.000 --> 01:42:32.000
Não era só isso mesmo, mas essa parte de de atendimento conjunto tem possibilidade de se inserir de alguma maneira.

01:42:32.000 --> 01:43:01.000
Então assim é. Porque, de fato, eu não sei como que isso funcionaria na prática o cenário prático, porque o cenário que eu imagino que é o que aconteça, é exatamente o que acontece hoje e que atende agora o de três ou quatro ou cinco pessoas atenderem ao mesmo tempo isso ficar ali para cinco ou seis pessoas ao mesmo tempo hoje não existe não há previsão para que a gente construa algo nesse sentido, gente pode fazer

01:43:01.000 --> 01:43:09.000
adaptações para que vocês. Cheguem mais próximo disso. Ou que pelo menos, armazenem essa informação.

01:43:09.000 --> 01:43:14.000
Sistema já permite que várias pessoas atendam essa pessoa, que ia ao mesmo tempo, né? Então eu não sei como que isso funcionaria.

01:43:14.000 --> 01:43:34.000
De fato, na prática, quando você fala que tem o atendimento em grupo psicólogo com a mesma pessoa ali numa sala, os três fazendo uma escuta ao mesmo tempo.

01:43:34.000 --> 01:43:35.000
Entendi. Não.

01:43:35.000 --> 01:43:39.000
Isso. Exato, porque aí a gente, cada um está trazendo como a gente tem um atendimento interdisciplinar.

01:43:39.000 --> 01:43:49.000
Existem alguns momentos em que mais um especialista está presente em atendimento, às vezes para coletar e ter justamente essa escolha técnica.

01:43:49.000 --> 01:43:58.000
Aham!

01:43:58.000 --> 01:44:10.000
Entendi.

01:44:10.000 --> 01:44:11.000
Uhum.

01:44:11.000 --> 01:44:27.000
Ao mesmo tempo. E as atividades coletivas, porque as atividades coletivas são desenvolvidas e que são aplicadas por mais de uma especialidade, geralmente para dar um apoio para as crianças pra que tem um psicólogo, por exemplo, pra coletar algumas informações para atendimento individual, são várias questões que são levantadas eu estou te perguntando isso também porque outra dúvida, que eu tinha era a partir do sistema irres seriam retirados por

01:44:27.000 --> 01:44:40.000
Uhum.

01:44:40.000 --> 01:44:41.000
Uhum.

01:44:41.000 --> 01:44:46.000
exemplo, as sinops, que são as quantidades de atendimento, já que tem a geração dos relatórios e aí, por isso, a minha preocupação de ter essa fita dignidade, de se perceber o atendimento de mais de um especialista, por exemplo, porque hoje, a gente entrega a sinopse detalhada São Paulo mas aí pode, parecer por exemplo, que determinado especialista se não foi ele que registrou não fez nada naquele dia, de

01:44:46.000 --> 01:44:49.000
Entendi, entendi.

01:44:49.000 --> 01:45:00.000
atendimento específico ou que aquela mulher vivenciou o momento, por exemplo, de atendimento coletivo mais de uma vez, quando, na verdade, tudo aconteceu ao mesmo tempo, entende?

01:45:00.000 --> 01:45:01.000
Seu filho? Claro.

01:45:01.000 --> 01:45:03.000
Eu entendo. Eu entendo completamente. E.

01:45:03.000 --> 01:45:12.000
Inclusive tem duas atividades que as vezes acontece ao mesmo tempo. João, uma com as mulheres e outra com os dependentes, com as crianças.

01:45:12.000 --> 01:45:17.000
Então a equipe está toda dividida. Todo mundo trabalhando. E a preocupação é como ficaria esse registro?

01:45:17.000 --> 01:45:18.000
Ok, sobre essa questão de dependentes e de mulheres. Pessoas atendidas. Já está Ok? E é assim que o sistema funciona.

01:45:18.000 --> 01:45:35.000
Você pode fazer o mesmo atendimento alego em locais diferentes ou no mesmo setor, por pessoas diferentes. Não tem essa restrição em grupo.

01:45:35.000 --> 01:45:42.000
Eu entendi bem o que a Juliana me falou. Faz total sentido. E aí, Juliana? Eu acho que é o seguinte.

01:45:42.000 --> 01:45:56.000
Eu vou construir algumas situações aqui, na prática. E a gente vai conversando nesse período. De como vocês podem fazer no dia a dia, para preencher isso no sistema, porque é possível, não é?

01:45:56.000 --> 01:46:06.000
Possível. No ato do atendimento inicial eu já ter, naquele momento, quatro ou cinco pessoas. Mas o que é possível?

01:46:06.000 --> 01:46:25.000
Quatro ou cinco pessoas diferentes, inserir informações no mesmo atendimento. E isso construiu um histórico. Rio de Janeiro. Situação daquele escopo do atendimento.

01:46:25.000 --> 01:46:37.000
Tá ai. Agora essa questão de naquele momento, ali naquele ciclo foi encerrado ali já ter quatro ou cinco pessoas hoje.

01:46:37.000 --> 01:46:46.000
Não existe lá dentro dele, mas a gente pode construir alternativas para que seja de fato levado em consideração esse cenário.

01:46:46.000 --> 01:46:58.000
Eu entendi perfeitamente. Passou. A gente vai alinhando e conversando. Essa questão nesse período de implementação, beleza.

01:46:58.000 --> 01:46:59.000
Muito.

01:46:59.000 --> 01:47:05.000
Jorge Siane perguntou sobre se os registros diários, ou seja, as atividades de rotina da mulher e seus filhos não serão registrados nesse sistema.

01:47:05.000 --> 01:47:19.000
Qual é a questão? Vamos lá. Isso é um ponto bastante interessante. O que está dentro do sistema aí hoje é o que é pertinente ao atendimento propriamente dito ao escopo ali daquele atendimento daquela responsabilidade.

01:47:19.000 --> 01:47:20.000
Quando eu estive na casa, eu vi que vocês têm as evoluções que vão inserindo das atividades.

01:47:20.000 --> 01:47:37.000
E às vezes, por nove e meia. Entreguei. Foi entregue no sabonete dez horas. Ela foi entregue em uma toalha.

01:47:37.000 --> 01:47:46.000
Informações não são importantes. Não, não estou eu estou dizendo que não são atendimentos. Também não estou. Não é minha responsabilidade.

01:47:46.000 --> 01:48:05.000
Questão é que a gente precisa e deve isso com total apoio da auto gestão dentro do sistema. A gente tem que fechar um ciclo de atendimento e definir o que é ou não é atendimento dentro do sistema a gente pode colocar um campo para evolução administrativa por exemplo, na casa da mulher brasileira hoje os agentes sociais, fazem isso então o que aconteceria essas evoluções podem.

01:48:05.000 --> 01:48:18.000
Por favor. Sim, sim, estamos sozinho. Por isso são eles mesmos também. Não aí você coloca um ataque.

01:48:18.000 --> 01:48:45.000
Essas evoluções podem estar sendo inseridas lá dentro. Só que assim é. Uma discussão bastante complicada, porque eu vi muita coisa lá que pertence ao dia a dia da casa, a rotina da casa, às vezes informações que poderiam estar sendo suprimidas em uma só foram colocadas em vários períodos então a princípio, essas informações ali que é o check List no plantão a evolução do

01:48:45.000 --> 01:48:59.000
plantão. Essas revoluções administrativas, além do dia a dia. A princípio, não ficariam aqui dentro a menos que a gente acha uma maneira eficaz de se fazer.

01:48:59.000 --> 01:49:12.000
A criação desses itens aqui dentro. Justamente porque a gente não consegue dizer. E não há um escopo definido para o que é ou não é atendimento.

01:49:12.000 --> 01:49:17.000
E eu, como representante da tecnologia, eu não posso chegar pra você. Que é especialista na sua área e dizer o que é, o que não é.

01:49:17.000 --> 01:49:29.000
Não tenho autonomia para isso. Por isso que a gente dentro do sistema, a gente tem um fluxo e esse fluxo tem que ser seguido.

01:49:29.000 --> 01:49:38.000
E aí, o que vocês tiverem de sugestão de adaptação pra gente colocar a gente vai tentar adaptar e colocar o mais próximo possível do que já existe.

01:49:38.000 --> 01:49:41.000
Hoje entendeu?

01:49:41.000 --> 01:49:44.000
O Gustavo Reis pergunta o sistema irá excluir a necessidade de mantermos as pastas.

01:49:44.000 --> 01:49:55.000
A relação das abrigadas, entradas e saídas das abrigadas. É o que se respondeu, né?

01:49:55.000 --> 01:49:56.000
Porque.

01:49:56.000 --> 01:50:05.000
É. Eu acho que é. Eu acho que é sobre essa questão de documento. Isso aí é com a alta gestão, e eu entendo também que vai levar um processo.

01:50:05.000 --> 01:50:15.000
Vocês vão ter que aprender a utilizar. Vão ter que testar. Vão ter que validar e a gente vai ter que aprovar, consolidar essas informações pra ver o que faz com essas documentações.

01:50:15.000 --> 01:50:19.000
Aí já não pagam muito a mão.

01:50:19.000 --> 01:50:35.000
A medida que vocês foram tendo dúvidas durante os testes, vocês vão reportando. A Renata. Tentei chegar num consenso e falou assim, que deve ser.

01:50:35.000 --> 01:50:39.000
Passa pra gente pra gente analisar e ver o que a gente pode pode acrescentar, fazer essas alterações no íris.

01:50:39.000 --> 01:50:54.000
Eu estou vendo aqui. Que a Renata já mandou para mim a relação de vocês com os perfis a gente vai fazer esse cadastro.

01:50:54.000 --> 01:50:57.000
João. Se acho que dá para liberar esse cadastro em dia.

01:50:57.000 --> 01:50:58.000
Da segunda.

01:50:58.000 --> 01:51:09.000
Segunda a sexta feira das oito por link Dois.

01:51:09.000 --> 01:51:10.000
Pode falar, Juliana.

01:51:10.000 --> 01:51:12.000
Temos uma dúvidazinha. Estranho.

01:51:12.000 --> 01:51:13.000
Tá.

01:51:13.000 --> 01:51:21.000
Não. Sim, eh. Só finalizar. A gente vai passar o link para vocês do grupo Pra Renata para ela já passar pra vocês pra vocês irem testando.

01:51:21.000 --> 01:51:51.000
Então a ideia é a primeira semana. Vocês fazem testes, fazem testes no sistema na segunda semana, a gente vai começar com o treinamento com vocês, ainda fazendo testes então são mais ou menos aí duas semanas pra vocês fazerem os testes nos no sistema e já no treinamento já chegarem já com sugestões dicas e que vai ser sem ser a próxima semana na outra para gente consolidar tudo e começar a funcionar de vez

01:51:53.000 --> 01:51:55.000
com íris, tá? Então semana que vem, vocês começam a fazer testes na outra semana. A gente vai dar o treinamento.

01:51:55.000 --> 01:52:25.000
Vai ser um por dia. Então a gente vai pegar. Vai na casa, abrigo e vai pegar cada equipe e vai dar um treinamento do íris e até lá, se vocês já puderem, anotar essas sugestões, e é isso a gente, precisa que cheguem no consenso também será que isso vai ser sigiloso não esse campo, tem que acrescentar não tem escrevam conversem com a Renata cheguem no

01:52:27.000 --> 01:52:35.000
consenso. Conversem entre dois, três especialistas, conversem com a Renata cheguem no consenso e passem pra gente, tá?

01:52:35.000 --> 01:52:38.000
Mas pode falar, Juliana.

01:52:38.000 --> 01:53:08.000
A desculpa só porque eu queria pegar esse último momento aí do que a Joyce tinha colocado. Eu achei muito interessante que o João falou da possibilidade de estudar essa evolução administrativa, porque o que acontece realmente eu entendo que vocês não compreendem como algo simples foi lá pegar um sabonete, só que às vezes as mulheres é muito comum que as mulheres entrem em conflito entre elas por coisas muito muito simples e algumas dessas

01:53:08.000 --> 01:53:38.000
coisas elas são percebidas justamente numa fala dessa mulher no balcão. Quando um servidor está passando em determinado momento, e aí presencia uma fala, alguma coisa que não chegou a ser uma ofensa, mas que vai ser muito importante, para que a equipe tome conhecimento para ficar mais atenta em relação a como vai se portar com aquela mulher o olhar que vai ter para ela vai estar mais próximo para uma possível mediação de conflitos,

01:53:38.000 --> 01:53:45.000
né? E esses indícios, essas pequenas coisas hoje, pra gente também é um réu, um respaldo.

01:53:45.000 --> 01:53:57.000
Porque traz um histórico desses detalhes muito específicos do dia a dia. Porque o nosso equipamento tem muito essa característica de casa, mesmo de algo doméstico.

01:53:57.000 --> 01:54:27.000
Mesmo e isso nos auxilia na conta, na comunicação entre plantões. Como realmente trazer esse histórico mais aprofundado pra estudo os estudos de caso que são realizados e aí, se for realmente possível, de colocar a parte não sei esse documento evolução administrativa onde os cuidadores os agentes sociais, ou mesmo os especialistas pudessem evoluir esses pormenores tanto de entrega de material quanto de por ter

01:54:47.000 --> 01:54:48.000
Hum.

01:54:48.000 --> 01:54:59.000
presenciado uma fala ou alguma coisa. Uma criança que chegou com um comentário que a gente já descobriu, inclusive necessidade de intervenção do Conselho tutelar em falas de crianças dentro da casa, de maneira completamente informal, descobrimos questões de abuso que elas tinham sofrido então são realmente coisas muito importantes, que estejam de fato, em registro então se for possível colocar eu acho que vai ser realmente muito muito importante pra.

01:54:59.000 --> 01:55:01.000
Não é? Oi.

01:55:01.000 --> 01:55:27.000
João essa pergunta. Isso que a Juliana colocou em complemento solidário para idosos que, perguntando se esses registros diário diárias no desligamento da mulher precisará ser anexada ao sistema a juliana, falou que ia ser importante mas assim são aqueles registros que você juliana, é aqueles registros que vocês passam de um plantão para o outro.

01:55:27.000 --> 01:55:28.000
Existe. O que é passado é mais um cenário, né? Mas dentro do decorrer do dia, a gente tem uma evolução minuciosa.

01:55:28.000 --> 01:55:46.000
Então, por exemplo, a criança tá lá brincando com outra. E aí a gente escutou que ela falou: Ah, pois.

01:55:46.000 --> 01:55:47.000
Hum.

01:55:47.000 --> 01:56:08.000
O meu pai fez assim assim no meu corpo, dando exemplo certo, aquilo ali não se configura como atendimento, porque ela não está dentro de um contexto de atendimento, mas foi uma fala foi presenciada por um servidor e muito importante também então isso precisa ser colocado a termo né?

01:56:08.000 --> 01:56:09.000
Sim.

01:56:09.000 --> 01:56:28.000
Então todas as coisas compõem. Na verdade, esse atendimento geral da mulher. Mesmo a entrega de um sabonete, às vezes as mulheres entram em conflito por conta da vez que vai lavar na lavanderia que a fulana pegou o que eu tinha separado pra mim e aquilo ali gera uma necessidade de mediação de conflito às vezes até ameaças eu de uma mulher com outra então é importante que

01:56:28.000 --> 01:56:47.000
todo esse histórico, por mais que seja simples e não seja necessariamente caracterizado como atendimento, ele esteja registrado, porque até uma forma de respaldo para a equipe e para fomentar os estudos, de caso são realmente muito preciosos observando essas questões expor menores entendeu?

01:56:47.000 --> 01:56:52.000
Com certeza. Aí, Juliana. Só colocando um adendo aqui é muito importante. Essa sua fala.

01:56:52.000 --> 01:57:03.000
Porque hoje, na casa da mulher brasileira, a gente já tem esse local de observação administrativa. Vocês podem definir.

01:57:03.000 --> 01:57:11.000
Já consegui pensar. Em mais ou menos duas ou três soluções que eu vou construir aqui dentro para ver o que é mais viável para vocês fazerem.

01:57:11.000 --> 01:57:25.000
Eu entendo que é extremamente importante vocês terem esse histórico. Aí a gente vai criar um campo a mais para que vocês consigam serem isso.

01:57:25.000 --> 01:57:54.000
Mas eu entendo que às vezes, no mesmo dia, pode ser inserido muita coisa. Consultar o histórico dessa pessoa vai ficar uma coisa gigante, ou a gente pode pegar e inserir esse documento como anexo a evolução administrativa do dia vinte do dez beleza no outro dia eu que vou fazer o atendimento dessa pessoa vejo na Avenida Juliana seria a evolução dela e vejo todos esses por menores

01:57:54.000 --> 01:57:55.000
essas questões minuciosas eu falo dessa questão do registro diário porque pra gente, sempre foi muito difícil para o gabinete.

01:57:55.000 --> 01:58:06.000
É muito difícil para a coordenação. É difícil deles definirem o que é, o que não é atendimento, gente.

01:58:06.000 --> 01:58:11.000
Não está falando do que é menos ou mais importante, porque a gente precisou fechar um escopo inicial.

01:58:11.000 --> 01:58:12.000
Um fluxo inicial que atenda a casa. Abrigo e essas outras questões, por exemplo, essas questões minuciosas do dia a dia.

01:58:12.000 --> 01:58:36.000
Esse mapeamento do que acontece na casa. Essas questões que têm que ser passadas para o dia seguinte, para outro ou servidor.

01:58:36.000 --> 01:58:37.000
Desesperada.

01:58:37.000 --> 01:58:41.000
Há soluções para que contempem essa questão. Isso já está previsto e hoje, na casa da mulher brasileira, já existe uma evolução administrativa.

01:58:41.000 --> 01:58:42.000
Ah, a.

01:58:42.000 --> 01:58:46.000
Maravilha hoje na casa. Desculpa.

01:58:46.000 --> 01:58:51.000
Falar que hoje na casa. O nome é registro de ar.

01:58:51.000 --> 01:58:52.000
Oi, Juliana. Que foi?

01:58:52.000 --> 01:58:59.000
Que São João. Na verdade, na verdade, é o que elas estão falando aí você é aquele prontuário. Aquele registro de evolução que você viu que a gente escreve tudo ali.

01:58:59.000 --> 01:59:04.000
Uhum.

01:59:04.000 --> 01:59:05.000
Tá.

01:59:05.000 --> 01:59:08.000
É. Eu.

01:59:08.000 --> 01:59:09.000
Uhum.

01:59:09.000 --> 01:59:10.000
É esse documento que a gente precisa pensar como fazer ele desse registro. Mesmo que a gente tá falando. Aquele que eu mostrei para vocês no dia da reunião, não estão lembrando só pra lembrar.

01:59:10.000 --> 01:59:22.000
Ok. Acredito até que acredito. Sim, Sim, acredito até que vocês possam pensar em algo até híbrido, às vezes, porque vai ter.

01:59:22.000 --> 01:59:31.000
Vai ter os anexos. Tem? Como você colocar esse anexo registro e esse anexo, esse registro lá em anexo no Íris, caso vocês queiram.

01:59:31.000 --> 01:59:38.000
Mas talvez algumas informações que têm nesse registro. Talvez vocês queiram e sereno íris. Talvez não. Tudo.

01:59:38.000 --> 01:59:47.000
Talvez não precise inserir tudo isso. Que vocês vão dizer pra gente. A medida que vocês forem mexendo nas informações, né?

01:59:47.000 --> 01:59:48.000
A medida que vocês forem mexendo no íris, vocês vão falando. Eu acho que falta isso aqui.

01:59:48.000 --> 02:00:01.000
Que eu preciso que acho que vai ser um atendimento. E aí você pode também anotar no seu registro lá e.

02:00:01.000 --> 02:00:07.000
Mas também pode colocar no íris depois, se quiserem, ainda pode anexar isso também no íris, como.

02:00:07.000 --> 02:00:37.000
Como. Como anexo. E aí isso que vocês vão definir nesses testes da próxima semana. Por que vocês vão inserir o que precisa ser alterado se vocês vão contar com atendimento ou não, a gente só achou que esse é como se fosse um livro de ocorrências de um dia para o outro a gente acha que esse livro essas ocorrências, em especial, não é claro tem muita coisa que pode ser colocada no íris

02:00:39.000 --> 02:00:44.000
mas acho que é uma coisa. A parte. Aí a gente tem que pensar nisso. E.

02:00:44.000 --> 02:00:54.000
E vão anexar no no sistema, ou vão deixar. Vai ser algum arquivo à parte só para passar para o próximo.

02:00:54.000 --> 02:01:00.000
O plantão e algumas daquelas informações. Vocês vão inserir no sistema como dados, para depois gerar dados.

02:01:00.000 --> 02:01:09.000
Como escrevendo, mesmo não só anexando. Então isso a gente tem que ver conforme o tempo for passando.

02:01:09.000 --> 02:01:13.000
Tá? Tem algumas perguntas aqui?

02:01:13.000 --> 02:01:40.000
Ah, e perguntas não, né? Mas a Juliana fala que é muito importante que esse registro seja editado, acho que como anexo não é interessante, somente após o desligamento da brigada, é isso que eu falei, gente precisa ver o que exatamente vocês querem que coloquem no sistema, Íris gente colocar essa evolução, e a gente não colocou nesse primeiro momento, essa evolução, é esse esse livro, de ocorrências que

02:01:40.000 --> 02:01:51.000
vocês fazem de um dia para o outro. Mas a gente vai conversando a respeito. E se vocês chegarem num consenso conversa com a gente também, pra gente ver a melhor forma.

02:01:51.000 --> 02:01:57.000
Tá bom. A Luciane fala que a evolução, assim como as saídas, é muito particular da casa.

02:01:57.000 --> 02:02:01.000
No caso, será compartilhado com outras unidades.

02:02:01.000 --> 02:02:06.000
Se vocês definirem que não, não será.

02:02:06.000 --> 02:02:07.000
E.

02:02:07.000 --> 02:02:18.000
Como a gente disse, aqui, tudo aqui dentro pode ser definido ou não como sigilo interno sigiloso.

02:02:18.000 --> 02:02:19.000
É aqui.

02:02:19.000 --> 02:02:25.000
Já é agora falo de sigilo. A Joyce. Ela tinha falado sobre essa questão de ser editada. E é, tá.

02:02:25.000 --> 02:02:30.000
Os campos de evolução técnica e evolução administrativa da casa da mulher brasileira são editais.

02:02:30.000 --> 02:02:38.000
Nossa preocupação é a seguinte: como o volume de dados da casa abrigo é muito grande o que é um nível de detalhamento muito grande.

02:02:38.000 --> 02:02:48.000
É? Não fica viável e não é visivelmente legal que vocês fiquem inserindo, editando essas informações todas no mesmo lugar.

02:02:48.000 --> 02:02:56.000
Por isso que a gente está com esse dilema aqui. Essa missão para poder resolver. Tá mas é edital.

02:02:56.000 --> 02:02:59.000
Sim.

02:02:59.000 --> 02:03:02.000
Pessoal, mais perguntas. A gente deixou de responder alguma.

02:03:02.000 --> 02:03:03.000
O Cláudio perguntou, caso ele seja implantado, incluindo os registros administrativos administrativos, seriam dispensáveis.

02:03:03.000 --> 02:03:19.000
Desses registros da pasta da casa. Abrigo da rede. O intuito é que daqui um tempo, seja assim.

02:03:19.000 --> 02:03:29.000
O sonho é que seja. Sim, mas a gente precisa de muitos degraus ainda pra poder chegar lá. Gente tem que consolidar esse sistema.

02:03:29.000 --> 02:03:59.000
Os servidores já têm que estar ambientado. Essa informação provavelmente tem que estar no seio. E tem também outras coisas pertinentes a Lgbt, que são informações que às vezes podem servir até como investigação como prova de um crime alguma coisa específica então essa questão toda tem que ser tratada com alta gestão nosso intuito é centralizar esses dados centralizar essa informação informação criptografada segura com punido de

02:03:59.000 --> 02:04:07.000
acesso e sistematizado. Que vai ser feito com esse documento. Aí é outro assunto, mesmo.

02:04:07.000 --> 02:04:17.000
Eu já entendi que o Cláudio perguntou sobre os sobre os prontuários passados. Assim, os registros que já foram feitos. Tá?

02:04:17.000 --> 02:04:21.000
O que eu entendo é que a gente vai começar agora do do zero. A gente vai começar a cadastrar as pessoas.

02:04:21.000 --> 02:04:34.000
As mulheres que estejam hoje na casa abrigo. As passadas. Aí, a gente precisa, pelo que a Valéria falou, estão combinando aí.

02:04:34.000 --> 02:04:42.000
Depois conversem com a gestão de subir. Isso para o sei. Então, eu queria que a gente vai começar a do zero.

02:04:42.000 --> 02:05:11.000
O cadastro de quem já está na unidade de quem vai chegar na unidade dos que estavam na unidade. Aí vai ter um outro direcionamento que eu acredito que seja essa digitalização ou no caso se já estão nas pastas não sei nesse caso, que, a Valéria, o que decidiram com a Valéria, se vão pegar de transformar o Pdf e jogar também para um processo sigiloso não sei mas a gente vai começar

02:05:11.000 --> 02:05:41.000
do zero. Vamos começar a cadastrar. Quem está na casa abrigo e quem vai chegar após outra questão, o período de testes que as próximas duas semanas são dados que vocês vão seria que vão se perder vocês podem testar é tudo tudo que precisar faz façam todos os testes necessários para depois falar os erros as sugestões então podem escrever porque depois quando a gente lançar o definitivo aí Sim, já

02:05:41.000 --> 02:05:50.000
vai ser a. Já vai ser o oficial. Mais alguma dúvida, pessoal? Mais alguma pergunta?

02:05:50.000 --> 02:05:56.000
É Rodrigo? Em relação aos prontuários antigos. Isso a gente vai decidir depois. Tá bom.

02:05:56.000 --> 02:05:57.000
Ok.

02:05:57.000 --> 02:06:00.000
Beleza.

02:06:00.000 --> 02:06:04.000
Mas agora.

02:06:04.000 --> 02:06:34.000
Então vamos fazer o seguinte. Fica combinado. Então, segunda feira, a gente passa os passando o acesso para todo mundo com o Comitê ao teste de vocês duas semanas de teste, a gente vai enviar um termo de compromisso para vocês a assinarem comprometendo com o sigilo dos dados e aí no caso seriam vocês e a Renata assinaria também então vai ser tudo ao mesmo tempo, então nas duas próximas semanas.

02:06:43.000 --> 02:06:51.000
Vão ser? Quando vocês vão preencher o termo de compromisso? Vai ser o período do treinamento. E vai ser também o período do teste.

02:06:51.000 --> 02:07:04.000
Então a gente espera que que dê tudo certo aí. E não deixem de fazer os testes para depois tirarem as dúvidas no trecho.

02:07:04.000 --> 02:07:06.000
Tudo certo, João.

02:07:06.000 --> 02:07:17.000
Por mim, tudo certo. Agradecer a presença do pessoal, a paciência com as pessoas que eu falei hoje já educação e cordialidade.

02:07:17.000 --> 02:07:24.000
Lá, não estava muito acostumado com isso. Durante esse processo de implementação, eu acho que vai ser um sucesso.

02:07:24.000 --> 02:07:53.000
Contem comigo. Ontem com o Rodrigo. Vocês não estão sozinhos aqui. Não estão desamparados, e a gente não está aqui para ser um burocratização que está aqui para ser um facilitador sistema vai vir para melhorar muitas coisas e muitos processos e a gente vai fazer espaço a quase todo mundo junto obrigado aí bom feriado pra vocês.

02:07:53.000 --> 02:08:06.000
Ok, pessoal. Então, segunda feira a gente entra em contato com a Renata. Tá bom para passar o link do sistema e os acessos não tem um ótimo fim de tarde, e um bom final de semana para vocês.

02:08:06.000 --> 02:08:07.000
Aí!

02:08:07.000 --> 02:08:08.000
Valeu, valeu!

02:08:08.000 --> 02:08:09.000
Yeah. And.

02:08:09.000 --> 02:08:10.000
Até mais.

02:08:10.000 --> 02:08:14.000
É uma
"""

texto_filtrado = remover_linhas_com_timestamp(texto)
print(texto_filtrado)
