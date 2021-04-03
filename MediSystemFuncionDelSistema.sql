SET SERVEROUTPUT ON

CREATE OR REPLACE FUNCTION verificarCedulas(cedulaAVerificar varchar2)
return number
-- Declaracion de variables locales
    IS
    
    cedulaTemp varchar2(100);
    
    BEGIN
       select rtrim(cedulaPaciente) into cedulaTemp from appmedisystem_paciente
       where cedulaPaciente = cedulaAVerificar;
       
       IF CEDULATEMP IS NOT NULL
        THEN 
            RETURN 0;
        END IF;
        
    EXCEPTION
    -- Sentencias control de excepcion
        WHEN others
            then
            begin
                RETURN 1;
            end;
END;   

CREATE OR REPLACE FUNCTION retornarID(cedulaDada varchar2)
return number
-- Declaracion de variables locales
    IS
        idTemp number;
    BEGIN
       select rtrim(idPaciente) into idTemp from appmedisystem_paciente
       where cedulaPaciente = cedulaDada;
       
    return idTemp; 
END; 


create or replace trigger  triggerVefCedulas
before insert on appmedisystem_paciente
for each row
declare

    isIn number;
    idTemp number;
    
begin
    isIn := verificarcedulas(:NEW.cedulaPaciente);
    if isin = 0 then
        --NO ESTÁ  
        idTemp := retornarID(:NEW.cedulaPaciente);
        update appmedisystem_paciente set
        pesopaciente = :new.pesopaciente, generopaciente = :new.generoPaciente,
        nombrePaciente = :new.nombrePaciente, tipodesangrepaciente = :new.tipodesangrepaciente,
        cedulaPaciente = :new.cedulaPaciente, edadPaciente = :new.edadPaciente,
        alturaPaciente = :new.alturaPaciente where idPaciente = idTemp;
        
        delete appmedisystem_paciente where idPaciente = idTemp;
    end if;
end;
/