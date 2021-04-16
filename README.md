# AppMutantes

Para ejecutar la consulta de estadisticas por favor copiar y pegar en el navegador la URL
http://appmutantes-env.eba-vivxwjhn.us-east-1.elasticbeanstalk.com/stats

Para ejecutar la validaciond de la secuencia ADN 
mediante PostMan enviar a traves del metodo POST http://appmutantes-env.eba-vivxwjhn.us-east-1.elasticbeanstalk.com/mutant
una secuencia ADN con la sgte estructura en forma JSON, la secuencia debe ser una lista de NxN
{"dna" : ["ATGCGAA","CAGGTGG","TTCTGTA","ACAATGA","CGCCTAT","CTCCGCA","AAGTCAA"]}
