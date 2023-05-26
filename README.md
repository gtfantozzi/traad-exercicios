# traad-aisweb
Exercio 2 do teste da TRAAD

Exercício 2

Para todo aviador, é vital saber antes de qualquer vôo as condições meteorológicas dos aeródromos de partida ou de chegada,
assim como a existência de cartas disponíveis e horários de nascer e pôr do sol.
No Brasil, estas informações são disponibilizadas pelo site https://aisweb.decea.mil.br/.
Nesta página é possível encontrar links para cartas, horários do sol e as informações de TAF e METAR,
que são boletins meteorológicos codificados.

Escreva um código que leia no terminal o código ICAO qualquer de um aeródromo (SBMT = campo de marte, SBJD = aeroporto de jundiaí, etc...)
e imprima na tela:

    As cartas disponíveis
    Os horários de nascer e pôr do sol de hoje
    A informação de TAF e METAR disponíveis

Vale ressaltar que estas informações devem ser obtidas em tempo real do site, através de SCRAPPING.

Envie o código dos exercícios 1 e 2 assim como instruções para rodar o projeto.
Se possível, use container docker ou virtualenv para construção de ambiente separado.