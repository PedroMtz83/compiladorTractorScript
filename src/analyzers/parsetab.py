
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASIGNAR A_CADENA BOOL CADENA CAPTURAR CODIGO COMA COMENTARIO COMENZAR CORCHETE_DER CORCHETE_IZQ DECIMAL DICCIONARIO DIFERENTE DIVIDIDO DOS_PUNTOS ENTERO EXCEPCION FUNCION IDENTIFICADOR IGUAL INTENTAR LISTA LLAVE_DER LLAVE_IZQ MAS MAYOR MAYOR_IGUAL MENOR MENOR_IGUAL MENOS MIENTRAS MOSTRAR_EN_PANTALLA NO NUEVA_LINEA O PARA PARENTESIS_DER PARENTESIS_IZQ POR PUNTO_COMA RETORNA SI SINO TERMINAR Y\n    programa : COMENZAR bloque_codigo TERMINAR\n    \n    bloque_codigo : LLAVE_IZQ lista_declaraciones LLAVE_DER\n    \n    lista_declaraciones : lista_declaraciones declaracion \n                        | declaracion\n    \n    declaracion : tipo IDENTIFICADOR IGUAL expresion PUNTO_COMA\n                | expresion PUNTO_COMA\n                | si\n                | para\n                | mientras\n    \n    tipo : ENTERO\n         | DECIMAL\n         | BOOL\n         | LISTA\n         | DICCIONARIO\n    \n    expresion : expresion operador expresion\n              | PARENTESIS_IZQ expresion PARENTESIS_DER\n              | IDENTIFICADOR\n              | ENTERO\n              | DECIMAL\n              | BOOL\n              | CADENA\n              | lista\n    \n    operador : MAS\n             | MENOS\n             | POR\n             | DIVIDIDO\n             | IGUAL\n             | DIFERENTE\n             | MENOR\n             | MAYOR\n             | MENOR_IGUAL\n             | MAYOR_IGUAL\n             | Y\n             | O\n             | NO\n    \n    lista : LISTA menor_tipo LLAVE_IZQ valores_lista LLAVE_DER\n    \n    menor_tipo : MENOR IDENTIFICADOR MAYOR\n    \n    valores_lista : valores_lista COMA valor_lista\n                  | valor_lista\n    \n    valor_lista : ENTERO\n                | DECIMAL\n                | BOOL\n    \n    si : SI PARENTESIS_IZQ expresion PARENTESIS_DER bloque_codigo\n                  | SI PARENTESIS_IZQ expresion Y expresion PARENTESIS_DER bloque_codigo\n                  | SI PARENTESIS_IZQ expresion O expresion PARENTESIS_DER bloque_codigo\n                  | SI PARENTESIS_IZQ NO expresion PARENTESIS_DER bloque_codigo\n    \n    para : PARA PARENTESIS_IZQ tipo IDENTIFICADOR IGUAL expresion PUNTO_COMA expresion PUNTO_COMA expresion PARENTESIS_DER bloque_codigo\n    \n    mientras : MIENTRAS PARENTESIS_IZQ expresion PARENTESIS_DER bloque_codigo\n    '
    
_lr_action_items = {'COMENZAR':([0,],[2,]),'$end':([1,5,],[0,-1,]),'LLAVE_IZQ':([2,43,72,73,78,85,89,90,99,],[4,55,-37,4,4,4,4,4,4,]),'TERMINAR':([3,25,],[5,-2,]),'ENTERO':([4,6,7,11,12,13,19,25,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,50,51,52,53,55,59,74,75,79,81,82,86,87,91,93,94,95,97,100,],[14,14,-4,-7,-8,-9,46,-2,-3,-6,46,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,46,61,46,46,69,46,46,46,-5,69,-43,46,-48,-46,-44,-45,46,46,-47,]),'DECIMAL':([4,6,7,11,12,13,19,25,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,50,51,52,53,55,59,74,75,79,81,82,86,87,91,93,94,95,97,100,],[15,15,-4,-7,-8,-9,47,-2,-3,-6,47,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,47,62,47,47,70,47,47,47,-5,70,-43,47,-48,-46,-44,-45,47,47,-47,]),'BOOL':([4,6,7,11,12,13,19,25,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,50,51,52,53,55,59,74,75,79,81,82,86,87,91,93,94,95,97,100,],[16,16,-4,-7,-8,-9,48,-2,-3,-6,48,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,48,63,48,48,71,48,48,48,-5,71,-43,48,-48,-46,-44,-45,48,48,-47,]),'LISTA':([4,6,7,11,12,13,19,25,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,50,51,52,53,59,74,75,79,82,86,87,91,93,94,95,97,100,],[17,17,-4,-7,-8,-9,49,-2,-3,-6,49,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,49,64,49,49,49,49,49,-5,-43,49,-48,-46,-44,-45,49,49,-47,]),'DICCIONARIO':([4,6,7,11,12,13,25,26,28,51,79,82,87,91,93,94,100,],[18,18,-4,-7,-8,-9,-2,-3,-6,18,-5,-43,-48,-46,-44,-45,-47,]),'PARENTESIS_IZQ':([4,6,7,11,12,13,19,22,23,24,25,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,50,52,53,59,74,75,79,82,86,87,91,93,94,95,97,100,],[19,19,-4,-7,-8,-9,19,50,51,52,-2,-3,-6,19,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,19,19,19,19,19,19,-5,-43,19,-48,-46,-44,-45,19,19,-47,]),'IDENTIFICADOR':([4,6,7,8,11,12,13,14,15,16,17,18,19,25,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,44,50,52,53,59,60,61,62,63,64,74,75,79,82,86,87,91,93,94,95,97,100,],[9,9,-4,27,-7,-8,-9,-10,-11,-12,-13,-14,9,-2,-3,-6,9,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,56,9,9,9,9,77,-10,-11,-12,-13,9,9,-5,-43,9,-48,-46,-44,-45,9,9,-47,]),'CADENA':([4,6,7,11,12,13,19,25,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,50,52,53,59,74,75,79,82,86,87,91,93,94,95,97,100,],[20,20,-4,-7,-8,-9,20,-2,-3,-6,20,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,20,20,20,20,20,20,-5,-43,20,-48,-46,-44,-45,20,20,-47,]),'SI':([4,6,7,11,12,13,25,26,28,79,82,87,91,93,94,100,],[22,22,-4,-7,-8,-9,-2,-3,-6,-5,-43,-48,-46,-44,-45,-47,]),'PARA':([4,6,7,11,12,13,25,26,28,79,82,87,91,93,94,100,],[23,23,-4,-7,-8,-9,-2,-3,-6,-5,-43,-48,-46,-44,-45,-47,]),'MIENTRAS':([4,6,7,11,12,13,25,26,28,79,82,87,91,93,94,100,],[24,24,-4,-7,-8,-9,-2,-3,-6,-5,-43,-48,-46,-44,-45,-47,]),'LLAVE_DER':([6,7,11,12,13,25,26,28,67,68,69,70,71,79,82,87,88,91,93,94,100,],[25,-4,-7,-8,-9,-2,-3,-6,80,-39,-40,-41,-42,-5,-43,-48,-38,-46,-44,-45,-47,]),'PUNTO_COMA':([9,10,14,15,16,20,21,46,47,48,54,57,66,80,92,96,],[-17,28,-18,-19,-20,-21,-22,-18,-19,-20,-15,-16,79,-36,95,97,]),'MAS':([9,10,14,15,16,20,21,45,46,47,48,54,57,58,65,66,76,80,83,84,92,96,98,],[-17,30,-18,-19,-20,-21,-22,30,-18,-19,-20,30,-16,30,30,30,30,-36,30,30,30,30,30,]),'MENOS':([9,10,14,15,16,20,21,45,46,47,48,54,57,58,65,66,76,80,83,84,92,96,98,],[-17,31,-18,-19,-20,-21,-22,31,-18,-19,-20,31,-16,31,31,31,31,-36,31,31,31,31,31,]),'POR':([9,10,14,15,16,20,21,45,46,47,48,54,57,58,65,66,76,80,83,84,92,96,98,],[-17,32,-18,-19,-20,-21,-22,32,-18,-19,-20,32,-16,32,32,32,32,-36,32,32,32,32,32,]),'DIVIDIDO':([9,10,14,15,16,20,21,45,46,47,48,54,57,58,65,66,76,80,83,84,92,96,98,],[-17,33,-18,-19,-20,-21,-22,33,-18,-19,-20,33,-16,33,33,33,33,-36,33,33,33,33,33,]),'IGUAL':([9,10,14,15,16,20,21,27,45,46,47,48,54,57,58,65,66,76,77,80,83,84,92,96,98,],[-17,34,-18,-19,-20,-21,-22,53,34,-18,-19,-20,34,-16,34,34,34,34,86,-36,34,34,34,34,34,]),'DIFERENTE':([9,10,14,15,16,20,21,45,46,47,48,54,57,58,65,66,76,80,83,84,92,96,98,],[-17,35,-18,-19,-20,-21,-22,35,-18,-19,-20,35,-16,35,35,35,35,-36,35,35,35,35,35,]),'MENOR':([9,10,14,15,16,17,20,21,45,46,47,48,49,54,57,58,65,66,76,80,83,84,92,96,98,],[-17,36,-18,-19,-20,44,-21,-22,36,-18,-19,-20,44,36,-16,36,36,36,36,-36,36,36,36,36,36,]),'MAYOR':([9,10,14,15,16,20,21,45,46,47,48,54,56,57,58,65,66,76,80,83,84,92,96,98,],[-17,37,-18,-19,-20,-21,-22,37,-18,-19,-20,37,72,-16,37,37,37,37,-36,37,37,37,37,37,]),'MENOR_IGUAL':([9,10,14,15,16,20,21,45,46,47,48,54,57,58,65,66,76,80,83,84,92,96,98,],[-17,38,-18,-19,-20,-21,-22,38,-18,-19,-20,38,-16,38,38,38,38,-36,38,38,38,38,38,]),'MAYOR_IGUAL':([9,10,14,15,16,20,21,45,46,47,48,54,57,58,65,66,76,80,83,84,92,96,98,],[-17,39,-18,-19,-20,-21,-22,39,-18,-19,-20,39,-16,39,39,39,39,-36,39,39,39,39,39,]),'Y':([9,10,14,15,16,20,21,45,46,47,48,54,57,58,65,66,76,80,83,84,92,96,98,],[-17,40,-18,-19,-20,-21,-22,40,-18,-19,-20,40,-16,74,40,40,40,-36,40,40,40,40,40,]),'O':([9,10,14,15,16,20,21,45,46,47,48,54,57,58,65,66,76,80,83,84,92,96,98,],[-17,41,-18,-19,-20,-21,-22,41,-18,-19,-20,41,-16,75,41,41,41,-36,41,41,41,41,41,]),'NO':([9,10,14,15,16,20,21,45,46,47,48,50,54,57,58,65,66,76,80,83,84,92,96,98,],[-17,42,-18,-19,-20,-21,-22,42,-18,-19,-20,59,42,-16,42,42,42,42,-36,42,42,42,42,42,]),'PARENTESIS_DER':([9,20,21,45,46,47,48,54,57,58,65,76,80,83,84,98,],[-17,-21,-22,57,-18,-19,-20,-15,-16,73,78,85,-36,89,90,99,]),'COMA':([67,68,69,70,71,88,],[81,-39,-40,-41,-42,-38,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'bloque_codigo':([2,73,78,85,89,90,99,],[3,82,87,91,93,94,100,]),'lista_declaraciones':([4,],[6,]),'declaracion':([4,6,],[7,26,]),'tipo':([4,6,51,],[8,8,60,]),'expresion':([4,6,19,29,50,52,53,59,74,75,86,95,97,],[10,10,45,54,58,65,66,76,83,84,92,96,98,]),'si':([4,6,],[11,11,]),'para':([4,6,],[12,12,]),'mientras':([4,6,],[13,13,]),'lista':([4,6,19,29,50,52,53,59,74,75,86,95,97,],[21,21,21,21,21,21,21,21,21,21,21,21,21,]),'operador':([10,45,54,58,65,66,76,83,84,92,96,98,],[29,29,29,29,29,29,29,29,29,29,29,29,]),'menor_tipo':([17,49,],[43,43,]),'valores_lista':([55,],[67,]),'valor_lista':([55,81,],[68,88,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> COMENZAR bloque_codigo TERMINAR','programa',3,'p_programa','Analizador_Sintactico.py',23),
  ('bloque_codigo -> LLAVE_IZQ lista_declaraciones LLAVE_DER','bloque_codigo',3,'p_bloque_codigo','Analizador_Sintactico.py',30),
  ('lista_declaraciones -> lista_declaraciones declaracion','lista_declaraciones',2,'p_lista_declaraciones','Analizador_Sintactico.py',37),
  ('lista_declaraciones -> declaracion','lista_declaraciones',1,'p_lista_declaraciones','Analizador_Sintactico.py',38),
  ('declaracion -> tipo IDENTIFICADOR IGUAL expresion PUNTO_COMA','declaracion',5,'p_declaracion','Analizador_Sintactico.py',48),
  ('declaracion -> expresion PUNTO_COMA','declaracion',2,'p_declaracion','Analizador_Sintactico.py',49),
  ('declaracion -> si','declaracion',1,'p_declaracion','Analizador_Sintactico.py',50),
  ('declaracion -> para','declaracion',1,'p_declaracion','Analizador_Sintactico.py',51),
  ('declaracion -> mientras','declaracion',1,'p_declaracion','Analizador_Sintactico.py',52),
  ('tipo -> ENTERO','tipo',1,'p_tipo','Analizador_Sintactico.py',62),
  ('tipo -> DECIMAL','tipo',1,'p_tipo','Analizador_Sintactico.py',63),
  ('tipo -> BOOL','tipo',1,'p_tipo','Analizador_Sintactico.py',64),
  ('tipo -> LISTA','tipo',1,'p_tipo','Analizador_Sintactico.py',65),
  ('tipo -> DICCIONARIO','tipo',1,'p_tipo','Analizador_Sintactico.py',66),
  ('expresion -> expresion operador expresion','expresion',3,'p_expresion','Analizador_Sintactico.py',73),
  ('expresion -> PARENTESIS_IZQ expresion PARENTESIS_DER','expresion',3,'p_expresion','Analizador_Sintactico.py',74),
  ('expresion -> IDENTIFICADOR','expresion',1,'p_expresion','Analizador_Sintactico.py',75),
  ('expresion -> ENTERO','expresion',1,'p_expresion','Analizador_Sintactico.py',76),
  ('expresion -> DECIMAL','expresion',1,'p_expresion','Analizador_Sintactico.py',77),
  ('expresion -> BOOL','expresion',1,'p_expresion','Analizador_Sintactico.py',78),
  ('expresion -> CADENA','expresion',1,'p_expresion','Analizador_Sintactico.py',79),
  ('expresion -> lista','expresion',1,'p_expresion','Analizador_Sintactico.py',80),
  ('operador -> MAS','operador',1,'p_operador','Analizador_Sintactico.py',93),
  ('operador -> MENOS','operador',1,'p_operador','Analizador_Sintactico.py',94),
  ('operador -> POR','operador',1,'p_operador','Analizador_Sintactico.py',95),
  ('operador -> DIVIDIDO','operador',1,'p_operador','Analizador_Sintactico.py',96),
  ('operador -> IGUAL','operador',1,'p_operador','Analizador_Sintactico.py',97),
  ('operador -> DIFERENTE','operador',1,'p_operador','Analizador_Sintactico.py',98),
  ('operador -> MENOR','operador',1,'p_operador','Analizador_Sintactico.py',99),
  ('operador -> MAYOR','operador',1,'p_operador','Analizador_Sintactico.py',100),
  ('operador -> MENOR_IGUAL','operador',1,'p_operador','Analizador_Sintactico.py',101),
  ('operador -> MAYOR_IGUAL','operador',1,'p_operador','Analizador_Sintactico.py',102),
  ('operador -> Y','operador',1,'p_operador','Analizador_Sintactico.py',103),
  ('operador -> O','operador',1,'p_operador','Analizador_Sintactico.py',104),
  ('operador -> NO','operador',1,'p_operador','Analizador_Sintactico.py',105),
  ('lista -> LISTA menor_tipo LLAVE_IZQ valores_lista LLAVE_DER','lista',5,'p_lista','Analizador_Sintactico.py',112),
  ('menor_tipo -> MENOR IDENTIFICADOR MAYOR','menor_tipo',3,'p_menor_tipo','Analizador_Sintactico.py',118),
  ('valores_lista -> valores_lista COMA valor_lista','valores_lista',3,'p_valores_lista','Analizador_Sintactico.py',124),
  ('valores_lista -> valor_lista','valores_lista',1,'p_valores_lista','Analizador_Sintactico.py',125),
  ('valor_lista -> ENTERO','valor_lista',1,'p_valor_lista','Analizador_Sintactico.py',134),
  ('valor_lista -> DECIMAL','valor_lista',1,'p_valor_lista','Analizador_Sintactico.py',135),
  ('valor_lista -> BOOL','valor_lista',1,'p_valor_lista','Analizador_Sintactico.py',136),
  ('si -> SI PARENTESIS_IZQ expresion PARENTESIS_DER bloque_codigo','si',5,'p_si','Analizador_Sintactico.py',143),
  ('si -> SI PARENTESIS_IZQ expresion Y expresion PARENTESIS_DER bloque_codigo','si',7,'p_si','Analizador_Sintactico.py',144),
  ('si -> SI PARENTESIS_IZQ expresion O expresion PARENTESIS_DER bloque_codigo','si',7,'p_si','Analizador_Sintactico.py',145),
  ('si -> SI PARENTESIS_IZQ NO expresion PARENTESIS_DER bloque_codigo','si',6,'p_si','Analizador_Sintactico.py',146),
  ('para -> PARA PARENTESIS_IZQ tipo IDENTIFICADOR IGUAL expresion PUNTO_COMA expresion PUNTO_COMA expresion PARENTESIS_DER bloque_codigo','para',12,'p_para','Analizador_Sintactico.py',160),
  ('mientras -> MIENTRAS PARENTESIS_IZQ expresion PARENTESIS_DER bloque_codigo','mientras',5,'p_mientras','Analizador_Sintactico.py',167),
]
