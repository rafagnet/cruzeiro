Guerras Estelares 🎮
Sobre o Projeto

"Guerras Estelares" é um jogo simples desenvolvido em Python usando a biblioteca Pygame. Este projeto é um MVP (Produto Viável Mínimo) criado como parte de um projeto de PIT II. O objetivo é apresentar um jogo funcional que pode ser expandido com novas funcionalidades no futuro, receber feedback e reimplementar as sugestões com bugs consertados.

Funcionalidades Implementadas
🟢 Jogador

    O jogador controla uma nave que pode se mover horizontalmente e atirar projéteis.
    Controles:
        Seta Esquerda: Move para a esquerda.
        Seta Direita: Move para a direita.
        Barra de Espaço: Dispara projéteis.

🟢 Inimigos

    Uma lista de inimigos que se movimentam horizontalmente e descem um pouco ao atingir as bordas da tela.
    Quando um inimigo é destruído:
        Um novo inimigo aparece em uma posição aleatória.
        A pontuação do jogador aumenta.

🟢 Projéteis

    O jogador pode disparar projéteis para destruir os inimigos.
    Foi implementado um cooldown para limitar a taxa de disparos.

🟢 Placar

    Um placar é exibido no canto superior esquerdo da tela, mostrando a pontuação atual do jogador.

🟢 Sons

    Sons personalizados foram adicionados:
        Disparo: Som ao atirar.
        Impacto: Som ao destruir um inimigo.
        Música de Fundo: Música tocando continuamente durante o jogo.

Estrutura do Código
Arquivos de Áudio

Os arquivos de áudio estão localizados na pasta audio no mesmo diretório do código-fonte. Certifique-se de que a pasta contém:

    shoot.wav - Som de disparo.
    hit.wav - Som de impacto ao destruir inimigos.
    background.wav - Música de fundo.

Lógica Principal
Loop Principal

    O jogo segue um loop contínuo até que o usuário feche a janela.
    Dentro do loop, são realizadas as seguintes tarefas:
        Captura de Eventos: Verifica entrada do teclado.
        Atualização de Estado: Atualiza posição dos objetos (jogador, projéteis, inimigos).
        Detecção de Colisões: Verifica se um projétil atingiu um inimigo.
        Renderização: Redesenha a tela com todos os objetos e atualiza o placar.

Segurança na Manipulação de Listas

    Para evitar erros ao remover elementos das listas (projéteis ou inimigos), foi implementada uma abordagem segura:
        Iteração sobre cópias das listas (bullets[:] e enemies[:]).
        Uso de verificações para garantir que elementos só sejam processados se ainda estiverem na lista.

Melhorias e Limitações
Melhorias Feitas

    Placar Implementado:
        Um sistema simples para exibir e atualizar a pontuação do jogador.
        A pontuação aumenta a cada inimigo destruído.

    Correção de Bugs:
        Resolvido um crash causado pela remoção de projéteis e inimigos durante o loop principal.
        Adicionado controle de remoção seguro utilizando iterações sobre cópias das listas.

    Áudio Melhorado:
        Sons de disparo, impacto e música de fundo adicionam imersão ao jogo.

Limitações

    Este jogo é apenas um MVP (Produto Viável Mínimo) e, portanto:
        Gráficos Simples: Apenas retângulos são usados para representar os objetos.
        Jogabilidade Básica: Não há níveis, variação de inimigos ou sistema de vidas.
        Sem Salvamento: O jogo não armazena a pontuação ou possui tela de game over.

Possíveis Expansões

Caso deseje expandir o projeto, as seguintes ideias podem ser implementadas:

    Gráficos Melhores: Substituir retângulos por sprites e adicionar animações.
    Níveis e Dificuldade: Criar múltiplos níveis com aumento gradual de dificuldade.
    Sistema de Vidas: Permitir que o jogador sofra danos antes do game over.
    Pontuação Persistente: Salvar a pontuação máxima em um arquivo ou banco de dados.
    Mais Inimigos: Adicionar diferentes tipos de inimigos com comportamentos variados.
    Tela Inicial e Game Over: Criar menus para iniciar o jogo ou exibir a pontuação final.

Requisitos
Dependências

    Python 3.8 ou superior
    Pygame (instalável via pip install pygame)

Como Executar

    Certifique-se de que os arquivos de áudio estão na pasta audio no mesmo diretório do código.
    Execute o seguinte comando no terminal:

    python game.py

Aviso

Este jogo foi desenvolvido como parte de um trabalho acadêmico para demonstrar a criação de um jogo funcional. É um protótipo básico destinado ao aprendizado e não é otimizado para produção ou distribuição comercial.

    Desenvolvido por: rafagnet
    Projeto para a disciplina: PIT_CC II
    Universidade: Cruzeiro do Sul


