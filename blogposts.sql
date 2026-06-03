BEGIN TRANSACTION;

DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS comments;
DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    publication_date TEXT NOT NULL,
    body TEXT NOT NULL
);

CREATE TABLE comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    publication_date TEXT NOT NULL,
    content TEXT NOT NULL,
    FOREIGN KEY(post_id) REFERENCES posts(id) ON DELETE CASCADE
);

CREATE TABLE tags (
    post_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    PRIMARY KEY(post_id, name),
    FOREIGN KEY(post_id) REFERENCES posts(id) ON DELETE CASCADE
);

-- Blogpost 1
INSERT INTO posts (id, title, publication_date, body) VALUES (1, 'Vi er i VM! (Tror vi? Joda!)', '2026-05-15', 'Det har skjedd. Dommeren blåste av, og vi vant faktisk! Hele Ullevaal Stadion sto og gråt, inkludert pølseselgeren.\n\nErling mistet skoen sin på overtid, men på en eller annen måte snublet han ballen i mål med lilletåa uansett. Vi feirer med ekstra tykke skiver med brunost i kveld. Pakk ullsokkene, gutter, vi skal til VM!');
INSERT INTO tags (post_id, name) VALUES (1, 'Kvalifisering');
INSERT INTO tags (post_id, name) VALUES (1, 'Ullevaal');

-- Blogpost 2
INSERT INTO posts (id, title, publication_date, body) VALUES (2, '90 minutter med kollektiv hjertebank mot Spania', '2026-05-10', 'Spania spilte fantastisk tiki-taka, men vi spilte klassisk "håp og bønn". Leo Østigård blokkerte et skudd med ansiktet i det 84. minutt, noe som er veldig snilt av ham, men sikkert ganske vondt.\n\nResultatet holdt helt inn! Kampen endte 1-1, som betyr at vi snek oss videre på målforskjellen. Det var ikke pent, men det var veldig, veldig norsk.');
INSERT INTO tags (post_id, name) VALUES (2, 'Spania');
INSERT INTO tags (post_id, name) VALUES (2, 'Kampreferat');

-- Blogpost 3
INSERT INTO posts (id, title, publication_date, body) VALUES (3, 'Erling avslører den hemmelige VM-dietten', '2026-05-01', 'Journalistene fra utlandet spurte hva hemmeligheten bak de tre målene mot Skottland var. Svaret? Grandiosa og et glass kulturmelk før leggetid.\n\nDe trodde han tullet, men vi som kjenner ham vet at dette er ren vitenskap. Hvis vi vinner VM, må Stortinget gjøre lørdagsgratis Grandiosa til lov.');
INSERT INTO tags (post_id, name) VALUES (3, 'Erling');
INSERT INTO tags (post_id, name) VALUES (3, 'Kosthold');

-- Blogpost 4
INSERT INTO posts (id, title, publication_date, body) VALUES (4, 'Regnværet i Glasgow redder oss igjen', '2026-04-22', 'Skottene trodde de hadde en fordel fordi det regnet på Hampden Park. Men de glemte at det regner i Bergen 300 dager i året. Våre gutter følte seg som hjemme.\n\nMartin Ødegaard skled på en gjørmete flekk, men pasningen traff tilfeldigvis Alexander Sørloth rett i panna. 1-0 til oss! Takk til værgudene.');
INSERT INTO tags (post_id, name) VALUES (4, 'Skottland');
INSERT INTO tags (post_id, name) VALUES (4, 'Bortekamp');

-- Blogpost 5
INSERT INTO posts (id, title, publication_date, body) VALUES (5, 'Det taktiske geniet: Muren som falt feil vei', '2026-04-14', 'Under frisparket to Georgia prøvde muren vår å hoppe, men tre av spillerne snublet i hverandre og falt. Dette forvirret Georgias spiss så mye at han skjøt ballen rett ut over sidelinja.\n\nTreneren kalte det "avansert psykologisk posisjonering" på pressekonferansen. Vi kaller det flaks, men vi tar det!');
INSERT INTO tags (post_id, name) VALUES (5, 'Georgia');
INSERT INTO tags (post_id, name) VALUES (5, 'Taktikk');

-- Blogpost 6
INSERT INTO posts (id, title, publication_date, body) VALUES (6, 'Da maskoten vår nesten stoppet kampen', '2026-04-02', 'Vår kjære elg-maskot presterte å miste hodet sitt rett foran motstanderens keeper under oppvarmingen. Kampen ble forsinket i to minutter mens vi lette etter geviret.\n\nStemningen var litt klein, men keeperen ble såpass distrahert at han slapp inn et enkelt langskudd fem minutter senere. Maskoten er herved banens beste.');
INSERT INTO tags (post_id, name) VALUES (6, 'Humor');
INSERT INTO tags (post_id, name) VALUES (6, 'Maskot');

-- Blogpost 7
INSERT INTO posts (id, title, publication_date, body) VALUES (7, 'Ståles lykkejakke overlever nok en thriller', '2026-03-25', 'Landslagstreneren har brukt den samme slitte, grønne boblejakken i hele vinter. Den lukter visstnok gammel vaffel nå, men så lenge vi vinner, får ingen lov til å vaske den.\n\nDa Kypros reduserte til 2-1 på slutten, rev han av en knapp i ren nervøsitet. Vi spleiser på ny knapp hvis vi tar tre poeng i neste kamp også.');
INSERT INTO tags (post_id, name) VALUES (7, 'Trener');
INSERT INTO tags (post_id, name) VALUES (7, 'Overtro');

-- Blogpost 8
INSERT INTO posts (id, title, publication_date, body) VALUES (8, 'Vaffelpresset i garderoben ga resultater', '2026-03-12', 'Etter en elendig førsteomgang mot Kypros, lovet støtteapparatet varme vafler med rømme og syltetøy hvis gutta scoret to mål i andre omgang.\n\nDet tok nøyaktig fire minutter før Sørloth stanget inn det første. Ingenting motiverer en nordmann som lukten av nystekt bakverk. Kampen endte 3-1.');
INSERT INTO tags (post_id, name) VALUES (8, 'Kypros');
INSERT INTO tags (post_id, name) VALUES (8, 'Garderobe');

-- Blogpost 9
INSERT INTO posts (id, title, publication_date, body) VALUES (9, 'Billettsjokk: Hele Norge prøver å bestille samtidig', '2026-03-01', 'Nettsidene til FIFA krasjet fullstendig i morges da 4 millioner nordmenn prøvde å sikre seg billetter. Bestemor på 84 ringte meg og varmt spurte om "det derre internettet" var ødelagt.\n\nVi er klare for å invadere tribunene med flagg, kubjeller og altfor dyre matpakker.');
INSERT INTO tags (post_id, name) VALUES (9, 'Supporter');
INSERT INTO tags (post_id, name) VALUES (9, 'Billetter');

-- Blogpost 10
INSERT INTO posts (id, title, publication_date, body) VALUES (10, 'Drømmen starter: Tre poeng mot Georgia!', '2026-02-18', 'Første kamp i kvalifiseringen er over, og vi har faktisk tre poeng i sekken! Spillet var kanskje ikke helt vakkert, og forsvaret så tidvis ut som de lette etter blåbær i skogen, men seier er seier.\n\nNå ligger vi øverst på tabellen i nøyaktig tre dager. La oss nyte det så lenge det varer!');
INSERT INTO tags (post_id, name) VALUES (10, 'Georgia');
INSERT INTO tags (post_id, name) VALUES (10, 'Drømmen');

-- Additional comment
INSERT INTO comments (post_id, title, publication_date, content) VALUES (1, 'Husk Kvikk Lunsj!', '2026-05-16', 'Fantastisk innlegg! Men husk at gutta må pakke nok Kvikk Lunsj i kofferten, ellers takler de ikke varmen i VM!');

COMMIT;