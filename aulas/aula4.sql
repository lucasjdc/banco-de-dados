/*
create schema cfbcursos;
CREATE TABLE cliente(
	i_cliente_cliente INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	s_nome_cliente VARCHAR(50) NOT NULL,
	s_cpf_cliente VARCHAR(11) NOT NULL,
	d_nasc_cliente DATETIME
);
*/

/*drop schema cfbcursos;*/

/*drop table cliente;*/

/*ALTER TABLE cliente MODIFY COLUMN  s_nome_cliente VARCHAR(30);*/

/*ALTER TABLE cliente ADD i_tipo_cliente INT DEFAULT 1;*/

ALTER TABLE cliente DROP COLUMN i_tipo_cliente;
