SELECT 
        idCliente, 
        flTwitch, 
        qtdePontos 

FROM clientes 
WHERE flTwitch = 1 
AND qtdePontos >= 500 

ORDER BY qtdePontos