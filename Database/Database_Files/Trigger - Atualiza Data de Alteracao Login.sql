USE BD_AGENDA;

DELIMITER $$;
CREATE TRIGGER ALTERAR_REG_LOGIN_BU BEFORE
UPDATE ON LOGIN FOR EACH ROW

BEGIN
   SET NEW.DATA_ALTERACAO := NOW();
END $$;