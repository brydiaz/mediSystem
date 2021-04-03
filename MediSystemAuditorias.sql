
--TABLAS RESPECTIVAS PARA LA AUDITORIAS
drop table auditoriaPaciente;
Create table auditoriaPaciente(
  columna   varchar2(30),
  nuevo   varchar2(30),
  viejo varchar2(30),
  usuario varchar2(30),
  fecha TIMESTAMP,
  operacion  varchar2(30)
);

drop table auditoriaCita;
Create table auditoriaCita(
  columna   varchar2(30),
  nuevo   varchar2(30),
  viejo varchar2(30),
  usuario varchar2(30),
  fecha TIMESTAMP,
  operacion  varchar2(30)
);

drop table auditoriaDoctor;
Create table auditoriaDoctor(
  columna   varchar2(30),
  nuevo   varchar2(30),
  viejo varchar2(30),
  usuario varchar2(30),
  fecha TIMESTAMP,
  operacion  varchar2(30)
);

--TRIGGERS QUE VERIFICAN LA INSERCCION, UPDATE Y DELETE
CREATE OR REPLACE trigger triggerAuditoriaPaciente
BEFORE INSERT OR DELETE OR UPDATE ON APPMEDISYSTEM_PACIENTE
FOR EACH ROW
DECLARE
BEGIN
  --SE DEBEN INSERTAR EN LA TABLA CADA VALOR MODIFICADO, por cada columna
  IF INSERTING THEN
    INSERT INTO auditoriaPaciente (columna,nuevo,viejo, usuario, fecha, operacion) 
    VALUES('PESO',:NEW.pesoPaciente, Null , user, SYSTIMESTAMP, 'INSERT');  
    
    INSERT INTO auditoriaPaciente (columna,nuevo,viejo, usuario, fecha, operacion) 
    VALUES('GENERO',:NEW.generoPaciente, Null , user, SYSTIMESTAMP, 'INSERT');  
    
    INSERT INTO auditoriaPaciente (columna,nuevo,viejo, usuario, fecha, operacion) 
    VALUES('NOMBRE',:NEW.nombrePaciente, Null , user, SYSTIMESTAMP, 'INSERT');
    
    INSERT INTO auditoriaPaciente (columna,nuevo,viejo, usuario, fecha, operacion) 
    VALUES('TIPO DE SANGRE',:NEW.tipodesangrePaciente, Null , user, SYSTIMESTAMP, 'INSERT');  
  
    INSERT INTO auditoriaPaciente (columna,nuevo,viejo, usuario, fecha, operacion) 
    VALUES('CEDULA:',:NEW.cedulaPaciente, Null , user, SYSTIMESTAMP, 'INSERT');  
    
    
    INSERT INTO auditoriaPaciente (columna,nuevo,viejo, usuario, fecha, operacion) 
    VALUES('EDAD:',:NEW.edadPaciente, Null , user, SYSTIMESTAMP, 'INSERT');  
    
    INSERT INTO auditoriaPaciente (columna,nuevo,viejo, usuario, fecha, operacion) 
    VALUES('ALTURA:',:NEW.alturaPaciente, Null , user, SYSTIMESTAMP, 'INSERT');  
    
  ELSIF DELETING THEN
  
    INSERT INTO auditoriaPaciente (columna,nuevo,viejo, usuario, fecha, operacion)
    VALUES(NULL,NULL,:OLD.pesoPaciente, user, SYSTIMESTAMP, 'DELETE');
    
    
    INSERT INTO auditoriaPaciente (columna,nuevo,viejo, usuario, fecha, operacion)
    VALUES(NULL,NULL,:OLD.generoPaciente, user, SYSTIMESTAMP, 'DELETE');
    
    INSERT INTO auditoriaPaciente (columna,nuevo,viejo, usuario, fecha, operacion)
    VALUES(NULL,NULL,:OLD.nombrePaciente, user, SYSTIMESTAMP, 'DELETE');
    
    INSERT INTO auditoriaPaciente (columna,nuevo,viejo, usuario, fecha, operacion)
    VALUES(NULL,NULL,:OLD.tipodesangrePaciente, user, SYSTIMESTAMP, 'DELETE');
    
    INSERT INTO auditoriaPaciente (columna,nuevo,viejo, usuario, fecha, operacion)
    VALUES(NULL,NULL,:OLD.cedulaPaciente, user, SYSTIMESTAMP, 'DELETE');
    
    INSERT INTO auditoriaPaciente (columna,nuevo,viejo, usuario, fecha, operacion)
    VALUES(NULL,NULL,:OLD.edadPaciente, user, SYSTIMESTAMP, 'DELETE');
    
    INSERT INTO auditoriaPaciente (columna,nuevo,viejo, usuario, fecha, operacion)
    VALUES(NULL,NULL,:OLD.alturaPaciente, user, SYSTIMESTAMP, 'DELETE');
    
    
    
  ELSIF UPDATING THEN
  
    INSERT INTO auditoriaPaciente (columna,nuevo,viejo, usuario, fecha, operacion) 
    VALUES('PESO',:NEW.pesoPaciente, :OLD.pesoPaciente, user, SYSTIMESTAMP,'UPDATE');
    
    INSERT INTO auditoriaPaciente (columna,nuevo,viejo, usuario, fecha, operacion) 
    VALUES('GENERO',:NEW.generoPaciente, :OLD.generoPaciente, user, SYSTIMESTAMP,'UPDATE');
    
    INSERT INTO auditoriaPaciente (columna,nuevo,viejo, usuario, fecha, operacion) 
    VALUES('NOMBRE',:NEW.nombrePaciente, :OLD.nombrePaciente, user, SYSTIMESTAMP,'UPDATE');
    
    INSERT INTO auditoriaPaciente (columna,nuevo,viejo, usuario, fecha, operacion) 
    VALUES('TIPO DE SANGRE',:NEW.tipodesangrePaciente, :OLD.tipodesangrePaciente, user, SYSTIMESTAMP,'UPDATE');
    
    INSERT INTO auditoriaPaciente (columna,nuevo,viejo, usuario, fecha, operacion) 
    VALUES('CEDULA',:NEW.cedulaPaciente, :OLD.cedulaPaciente, user, SYSTIMESTAMP,'UPDATE');
    
    INSERT INTO auditoriaPaciente (columna,nuevo,viejo, usuario, fecha, operacion) 
    VALUES('EDAD',:NEW.edadPaciente, :OLD.edadPaciente, user, SYSTIMESTAMP,'UPDATE');
    
    INSERT INTO auditoriaPaciente (columna,nuevo,viejo, usuario, fecha, operacion) 
    VALUES('ALTURA',:NEW.alturaPaciente, :OLD.alturaPaciente, user, SYSTIMESTAMP,'UPDATE');
  END IF;
END;
/


CREATE OR REPLACE trigger triggerAuditoriaCita
BEFORE INSERT OR DELETE OR UPDATE ON APPMEDISYSTEM_CITA
FOR EACH ROW
DECLARE
BEGIN
  --SE DEBEN INSERTAR EN LA TABLA CADA VALOR MODIFICADO, por cada columna
  IF INSERTING THEN
  
    INSERT INTO auditoriaCita(columna,nuevo,viejo, usuario, fecha, operacion) 
    VALUES('FECHA',:NEW.fechaCita, Null , user, SYSTIMESTAMP, 'INSERT');  
    
     INSERT INTO auditoriaCita(columna,nuevo,viejo, usuario, fecha, operacion) 
    VALUES('MOTIVO',:NEW.motivoCita, Null , user, SYSTIMESTAMP, 'INSERT');
    
     INSERT INTO auditoriaCita(columna,nuevo,viejo, usuario, fecha, operacion) 
    VALUES('ID PACIENTE',:NEW.pacientefk_id, Null , user, SYSTIMESTAMP, 'INSERT');


  ELSIF DELETING THEN
  
    INSERT INTO auditoriaCita (columna,nuevo,viejo, usuario, fecha, operacion)
    VALUES(NULL,NULL,:OLD.fechaCita, user, SYSTIMESTAMP, 'DELETE');
    
    INSERT INTO auditoriaCita (columna,nuevo,viejo, usuario, fecha, operacion)
    VALUES(NULL,NULL,:OLD.motivoCita, user, SYSTIMESTAMP, 'DELETE');
    
    INSERT INTO auditoriaCita (columna,nuevo,viejo, usuario, fecha, operacion)
    VALUES(NULL,NULL,:OLD.pacientefk_id, user, SYSTIMESTAMP, 'DELETE');
    
    
    
  ELSIF UPDATING THEN
  
    INSERT INTO auditoriaCita (columna,nuevo,viejo, usuario, fecha, operacion) 
    VALUES('PESO',:NEW.fechaCita, :OLD.fechaCita, user, SYSTIMESTAMP,'UPDATE');
    
    INSERT INTO auditoriaCita (columna,nuevo,viejo, usuario, fecha, operacion) 
    VALUES('PESO',:NEW.motivoCita, :OLD.motivoCita, user, SYSTIMESTAMP,'UPDATE');
    
    INSERT INTO auditoriaCita (columna,nuevo,viejo, usuario, fecha, operacion) 
    VALUES('PESO',:NEW.pacientefk_id, :OLD.pacientefk_id, user, SYSTIMESTAMP,'UPDATE');
    
 
  END IF;
END;
/

CREATE OR REPLACE trigger triggerAuditoriaDoctor
BEFORE INSERT OR DELETE OR UPDATE ON APPMEDISYSTEM_DOCTOR
FOR EACH ROW
DECLARE
BEGIN
  --SE DEBEN INSERTAR EN LA TABLA CADA VALOR MODIFICADO, por cada columna
  IF INSERTING THEN
  
    INSERT INTO auditoriaDoctor(columna,nuevo,viejo, usuario, fecha, operacion) 
    VALUES('ESPECIALIDAD',:NEW.especialidadDoctor, Null , user, SYSTIMESTAMP, 'INSERT');  
    
    INSERT INTO auditoriaDoctor(columna,nuevo,viejo, usuario, fecha, operacion) 
    VALUES('NOMBRE',:NEW.nombreDoctor, Null , user, SYSTIMESTAMP, 'INSERT');  
    

  ELSIF DELETING THEN
  
    INSERT INTO auditoriaDoctor (columna,nuevo,viejo, usuario, fecha, operacion)
    VALUES(NULL,NULL,:OLD.especialidadDoctor, user, SYSTIMESTAMP, 'DELETE');
    INSERT INTO auditoriaDoctor (columna,nuevo,viejo, usuario, fecha, operacion)
    VALUES(NULL,NULL,:OLD.nombreDoctor, user, SYSTIMESTAMP, 'DELETE');
    
 
    
    
    
  ELSIF UPDATING THEN
  
    INSERT INTO auditoriaDoctor (columna,nuevo,viejo, usuario, fecha, operacion) 
    VALUES('ESPECIALIDAD',:NEW.especialidadDoctor, :OLD.especialidadDoctor, user, SYSTIMESTAMP,'UPDATE');
    
    INSERT INTO auditoriaDoctor (columna,nuevo,viejo, usuario, fecha, operacion) 
    VALUES('NOMBRE',:NEW.nombreDoctor, :OLD.nombreDoctor, user, SYSTIMESTAMP,'UPDATE');

  END IF;
END;
/

