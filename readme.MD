Linux para reproduzir um bug que me foi relatado. Como na época, os downloads oficiais não ofereciam mais esta versão (e procurando uma solução não me deu, perguntei aqui ). Recebi uma resposta muito útil lá, que gostou de https://www.chromium.org/getting-involved/download-chromium

Vou copiar/colar as etapas relevantes dessa página aqui:

Baixando compilações antigas do Chrome / Chromium

Digamos que você queira uma compilação do Chrome 44 para fins de depuração. O Google não oferece compilações antigas, pois não possuem correções de segurança atualizadas.

No entanto, você pode obter uma compilação do Chromium 44.x que deve corresponder principalmente à versão estável. Veja como você o encontra:

Procure em https://googlechromereleases.blogspot.com/search/label/Stable%20updates a última vez "44". foi mencionado.
Faça um loop desse histórico de versão (" 4402403157 ") na pesquisa de posição
Neste caso, retorna uma posição base de "330231". Este é o commit de onde a versão 44 foi ramificada, em maio de 2015. (consulte a nota de rodapé)
Abra o arquivo de compilações contínuas
Clique na sua plataforma (Linux/Mac/Win)
Cole "330231" no campo de filtro na parte superior e aguarde todos os resultados para o XHR.
Eventualmente, obtenho um resultado perfeito: https://commondatastorage.googleapis.com/chromium-browser-snapshots/index.html?prefix=Mac/330231/ -- Às vezes, você pode ter que diminuir o número de confirmação até encontrar um.
Baixe e execute!
nota de rodapé: como esta compilação foi feita no ponto de ramificação 44, ela não possui nenhum commit mesclado durante a versão beta. Normalmente, tudo bem, mas se você precisar de uma compilação verdadeira de "44.0.2403.x", precisará compilar o Chromium a partir da ramificação 2403. Alguns sites PortableApps/PortableChromium oferecem binários como este, devido a questões de segurança, a equipe do Chrome não recomenda executá-los.

