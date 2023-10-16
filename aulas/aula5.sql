create table tipocliente(
	i_tipocliente_tipocliente INT PRIMARY KEY AUTO_INCREMENTE,
	s_dsctipocliente_tipocliente VARCHAR(100) NOT NULL
);

/*
ALTER TABLE <tabela_origem> ADD CONSTRAINT <nome_restrição> FOREING KEY <campo_tabela_origem> REFERENCES <tabela_destino> (<camp_tabela_destino>);
*/

alter table cliente add constraint fk_tipocliente FOREIGN KEY (i_tipo_cliente) references tipocliente (i_tipocliente_tipocliente);