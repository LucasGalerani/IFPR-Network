--USUARIOS
CREATE TABLE `usuario` (
    `nome` varchar(50) NOT NULL,
    `senha` varchar(150) NOT NULL,
    `cpf` varchar(15) NOT NULL,
    `email` varchar(50) DEFAULT NULL,
    `data_nasc` date NOT NULL,
    `data_entrada` int(10) unsigned NOT NULL,
    `numero_matricula` int(11) NOT NULL,
    PRIMARY KEY (`numero_matricula`),
    UNIQUE KEY `nome` (`nome`),
    UNIQUE KEY `cpf` (`cpf`)
) DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci

--PERGUNTAS
CREATE TABLE `pergunta` (
    `idpergunta` int(11) NOT NULL AUTO_INCREMENT,
    `titulo` varchar(150) DEFAULT NULL,
    `pergunta` varchar(350) DEFAULT NULL,
    `estudante` int(11) DEFAULT NULL,
    `categoria` varchar(6) NOT NULL,
    PRIMARY KEY (`idpergunta`),
    KEY `estudante` (`estudante`),
    CONSTRAINT `pergunta_ibfk_1` FOREIGN KEY (`estudante`) REFERENCES `usuario` (`numero_matricula`)
) DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci

--RESPOSTAS
CREATE TABLE `resposta` (
    `idresposta` int(11) NOT NULL AUTO_INCREMENT,
    `pergunta_referente` int(11) DEFAULT NULL,
    `estudante` int(11) DEFAULT NULL,
    `texto` varchar(150) DEFAULT NULL,
    PRIMARY KEY (`idresposta`),
    KEY `pergunta_referente` (`pergunta_referente`),
    KEY `estudante` (`estudante`),
    CONSTRAINT `resposta_ibfk_1` FOREIGN KEY (`pergunta_referente`) REFERENCES `pergunta` (`idpergunta`),
    CONSTRAINT `resposta_ibfk_2` FOREIGN KEY (`estudante`) REFERENCES `usuario` (`numero_matricula`)
) DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci