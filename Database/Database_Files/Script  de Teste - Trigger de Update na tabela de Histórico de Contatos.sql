USE BD_AGENDA;

-- DELETE CASO TENHA SIDO INSERIDOS OS REGISTROS ABAIXOS E PRECISEI REALIZAR MAIS TESTES
DELETE FROM CONTATOS WHERE ID_CONTATO = (SELECT MAX(ID_CONTATO)FROM CONTATOS);
DELETE FROM HISTORICO_CONTATOS WHERE ID_HISTORICO = (SELECT MAX(ID_HISTORICO) FROM HISTORICO_CONTATOS);
DELETE FROM LOGIN WHERE ID_LOGIN = (SELECT MAX(ID_LOGIN) FROM LOGIN);

-- INSERTS DE TESTE
 UPDATE CONTATOS
  SET NOME = 'TESTE 2'
  WHERE ID_CONTATO = 2;

SELECT * FROM LOGIN;
SELECT * FROM CONTATOS;
SELECT * FROM HISTORICO_CONTATOS;
SELECT * FROM HISTORICO_CONTATOS_DESC_V;
