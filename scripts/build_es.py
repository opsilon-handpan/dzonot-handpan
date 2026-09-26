#!/usr/bin/env python3
"""Build the Spanish page es/index.html from the English index.html.

Run from the repo root:  python3 scripts/build_es.py
Every English string below must exist in index.html; if one is missing
(because the English copy changed), the script stops and names it so the
translation can be updated instead of silently drifting.
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "index.html"
OUT = ROOT / "es" / "index.html"

# (english, spanish) — applied in order, each must match at least once.
T = [
    # --- head / SEO ---
    ('<html lang="en">', '<html lang="es">'),
    ('<title>SHIVAPAN Handpan Tulum, México | Handcrafted Handpans</title>',
     '<title>SHIVAPAN Handpan Tulum | Handpans hechos a mano en México</title>'),
    ('<meta name="description" content="Handcrafted handpan (hang drum) instruments made by Israel in Tulum, Quintana Roo, México — instruments available now, 10 scales, private visits in the Riviera Maya.">',
     '<meta name="description" content="Handpans hechos a mano en Tulum, Quintana Roo, por Israel. Instrumentos disponibles, 10 escalas y visitas privadas en Tulum, Riviera Maya. Hang drum artesanal hecho en México.">'),
    ('<link rel="canonical" href="https://shivapan.com/">', '<link rel="canonical" href="https://shivapan.com/es/">'),
    ('<meta property="og:title" content="SHIVAPAN Handpan — Tulum, México">',
     '<meta property="og:title" content="SHIVAPAN Handpan — Handpans hechos a mano en Tulum">'),
    ('<meta property="og:description" content="Handcrafted handpan instruments from Tulum, Riviera Maya, México.">',
     '<meta property="og:description" content="Handpans hechos a mano en Tulum, Quintana Roo. Instrumentos artesanales de la Riviera Maya.">'),
    ('<meta property="og:url" content="https://shivapan.com/">', '<meta property="og:url" content="https://shivapan.com/es/">'),
    ('<meta property="og:locale" content="en_US">\n<meta property="og:locale:alternate" content="es_MX">',
     '<meta property="og:locale" content="es_MX">\n<meta property="og:locale:alternate" content="en_US">'),
    ('<meta name="twitter:description" content="Handcrafted handpan instruments from Tulum, México.">',
     '<meta name="twitter:description" content="Handpans hechos a mano en Tulum, Quintana Roo.">'),

    # --- asset paths (page lives one folder down) ---
    ('src="images/', 'src="/images/'),
    ('href="images/', 'href="/images/'),
    ('"audio/pantam/"', '"/audio/pantam/"'),

    # --- nav ---
    ('<li><a href="#origin">Origin</a></li>', '<li><a href="#origin">Origen</a></li>'),
    ('<li><a href="#maker">The Maker</a></li>', '<li><a href="#maker">El Artesano</a></li>'),
    ('<li><a href="#available">Available</a></li>', '<li><a href="#available">Disponibles</a></li>'),
    ('<li><a href="#instruments">Scales</a></li>', '<li><a href="#instruments">Escalas</a></li>'),
    ('<li><a href="#player">Play</a></li>', '<li><a href="#player">Tocar</a></li>'),
    ('<li><a href="#articles">Knowledge</a></li>', '<li><a href="#articles">Conocimiento</a></li>'),
    ('<li><a href="#videos">Videos</a></li>', '<li><a href="#videos">Videos</a></li>'),
    ('<li><a href="#contact">Contact</a></li>', '<li><a href="#contact">Contacto</a></li>'),
    ('<li class="lang-switch"><a href="/es/" hreflang="es" lang="es">ES</a></li>',
     '<li class="lang-switch"><a href="/" hreflang="en" lang="en">EN</a></li>'),

    # --- hero ---
    ('<p class="hero-tagline">Born from the silence of the earth.<br>Crafted by the rhythm of the soul.</p>',
     '<p class="hero-tagline">Nacido del silencio de la tierra.<br>Forjado al ritmo del alma.</p>'),
    ('<a href="#instruments" class="btn">Discover the Sound</a>', '<a href="#instruments" class="btn">Descubre el sonido</a>'),

    # --- origin ---
    ('<h2 class="section-title">Shiva — Where Sound Begins</h2>', '<h2 class="section-title">Shiva — Donde nace el sonido</h2>'),
    ('<p class="section-subtitle">The drum that sets the universe in motion</p>',
     '<p class="section-subtitle">El tambor que pone en movimiento al universo</p>'),
    ('In Hindu tradition, Shiva dances the cosmic dance of creation, and in his hand he holds the <em>damaru</em> — a small drum whose rhythm is said to have awakened the first sounds of the universe. Every vibration, every note, every heartbeat is an echo of that first pulse.',
     'En la tradición hindú, Shiva baila la danza cósmica de la creación y en su mano sostiene el <em>damaru</em>, un pequeño tambor cuyo ritmo, se dice, despertó los primeros sonidos del universo. Cada vibración, cada nota, cada latido es un eco de ese primer pulso.'),
    ('SHIVAPAN instruments carry this same essence. Each one is a vessel of resonance, shaped from steel yet alive with the voice of something ancient and elemental. Born in Tulum, between the jungle and the sea, the handpan holds stillness at its center — and from that stillness, music is born.',
     'Los instrumentos SHIVAPAN llevan esa misma esencia. Cada uno es un recipiente de resonancia, moldeado en acero pero vivo con la voz de algo antiguo y elemental. Nacido en Tulum, entre la selva y el mar, el handpan guarda la quietud en su centro, y de esa quietud nace la música.'),

    # --- maker ---
    ('<h2 class="section-title">The Hands Behind the Sound</h2>', '<h2 class="section-title">Las manos detrás del sonido</h2>'),
    ('<p class="section-subtitle">Israel — Handpan maker, Tulum, México</p>',
     '<p class="section-subtitle">Israel — Artesano de handpans, Tulum, México</p>'),
    ('alt="Israel, handpan maker of SHIVAPAN, playing one of his handpans in Tulum, México"',
     'alt="Israel, artesano de handpans SHIVAPAN, tocando uno de sus handpans en Tulum, México"'),
    ("Israel is a handpan maker based in Tulum, México — one of the few artisans in the country dedicated to this craft. His journey began with a fascination for the handpan's unique voice and evolved into a deep commitment to creating instruments that embody the spirit of the land he calls home.",
     'Israel es un artesano de handpans radicado en Tulum, México, uno de los pocos en el país dedicados a este oficio. Su camino comenzó con la fascinación por la voz única del handpan y se transformó en un profundo compromiso: crear instrumentos que encarnen el espíritu de la tierra que llama hogar.'),
    ('Working in the heart of the Riviera Maya, surrounded by jungle, cenotes, and the remnants of ancient civilizations, Israel brings an unmistakable character to each instrument. Every SHIVAPAN handpan is hand-hammered, carefully tuned, and finished with the patience that only a maker who loves his craft can bring.',
     'Trabajando en el corazón de la Riviera Maya, rodeado de selva, cenotes y vestigios de civilizaciones antiguas, Israel le da a cada instrumento un carácter inconfundible. Cada handpan SHIVAPAN está martillado a mano, afinado con cuidado y terminado con la paciencia que solo un artesano que ama su oficio puede dar.'),
    ('His instruments are not mass-produced. Each one is created with intention, tuned to a specific scale, and made to be felt — not just heard.',
     'Sus instrumentos no se fabrican en serie. Cada uno se crea con intención, se afina en una escala específica y está hecho para sentirse, no solo para escucharse.'),

    # --- available ---
    ('<h2 class="section-title">Available Instruments</h2>', '<h2 class="section-title">Instrumentos disponibles</h2>'),
    ('<p class="section-subtitle">Handpans ready to find their player — D Minor (D Kurd 9)</p>',
     '<p class="section-subtitle">Handpans listos para encontrar a su músico — Re menor (D Kurd 9)</p>'),
    ('alt="SHIVAPAN handpan D Kurd 9 in stainless steel with ember finish"',
     'alt="Handpan SHIVAPAN D Kurd 9 de acero inoxidable con acabado ember"'),
    ('alt="SHIVAPAN handpan D Kurd 9 in dark nitrided steel"',
     'alt="Handpan SHIVAPAN D Kurd 9 de acero nitrurado oscuro"'),
    ('alt="SHIVAPAN handpan D Kurd 9 in stainless steel with ember finish, second instrument"',
     'alt="Handpan SHIVAPAN D Kurd 9 de acero inoxidable con acabado ember, segundo instrumento"'),
    ('<div class="scale-mayan">Stainless Ember · No. 1</div>', '<div class="scale-mayan">Inoxidable Ember · No. 1</div>'),
    ('<div class="scale-mayan">Nitrided Steel</div>', '<div class="scale-mayan">Acero nitrurado</div>'),
    ('<div class="scale-mayan">Stainless Ember · No. 2</div>', '<div class="scale-mayan">Inoxidable Ember · No. 2</div>'),
    ('<p>Stainless steel with a warm ember finish. Bright, clear tone with a long, singing sustain — and naturally resistant to rust and humidity, ideal for the tropical climate of the Riviera Maya.</p>',
     '<p>Acero inoxidable con un cálido acabado ember. Tono brillante y claro, con un sustain largo y cantado, y naturalmente resistente al óxido y la humedad: ideal para el clima tropical de la Riviera Maya.</p>'),
    ('<p>Classic nitrided steel with a deep, dark finish. A warm, round and intimate voice with a softer sustain — the traditional handpan sound, perfect for meditation and slow, expressive playing.</p>',
     '<p>Acero nitrurado clásico con un acabado oscuro y profundo. Una voz cálida, redonda e íntima, con un sustain más suave: el sonido tradicional del handpan, perfecto para la meditación y para tocar de forma lenta y expresiva.</p>'),
    ('Hola%21%20I%20am%20interested%20in%20the%20D%20Kurd%209%20Stainless%20Ember%20No.%201%20handpan.',
     'Hola%21%20Me%20interesa%20el%20handpan%20D%20Kurd%209%20Inoxidable%20Ember%20No.%201.'),
    ('Hola%21%20I%20am%20interested%20in%20the%20D%20Kurd%209%20Nitrided%20Steel%20handpan.',
     'Hola%21%20Me%20interesa%20el%20handpan%20D%20Kurd%209%20de%20acero%20nitrurado.'),
    ('Hola%21%20I%20am%20interested%20in%20the%20D%20Kurd%209%20Stainless%20Ember%20No.%202%20handpan.',
     'Hola%21%20Me%20interesa%20el%20handpan%20D%20Kurd%209%20Inoxidable%20Ember%20No.%202.'),
    ('>Reserve via WhatsApp</a>', '>Apartar por WhatsApp</a>'),
    ('data-subject="D Kurd 9 — Stainless Ember · No. 1">or send a message</a>',
     'data-subject="D Kurd 9 — Inoxidable Ember · No. 1">o envía un mensaje</a>'),
    ('data-subject="D Kurd 9 — Nitrided Steel">or send a message</a>',
     'data-subject="D Kurd 9 — Acero nitrurado">o envía un mensaje</a>'),
    ('data-subject="D Kurd 9 — Stainless Ember · No. 2">or send a message</a>',
     'data-subject="D Kurd 9 — Inoxidable Ember · No. 2">o envía un mensaje</a>'),
    ('<p class="available-note">Prices in Mexican pesos. Carrying bag included · Shipping not included · Visits in Tulum by appointment.</p>',
     '<p class="available-note">Precios en pesos mexicanos. Incluye funda · Envío no incluido · Visitas en Tulum con cita previa.</p>'),

    # --- scales ---
    ('<h2 class="section-title">The Scales</h2>', '<h2 class="section-title">Las escalas</h2>'),
    ('<p class="section-subtitle">Each scale is a world. Find the one that resonates with your story.</p>',
     '<p class="section-subtitle">Cada escala es un mundo. Encuentra la que resuena con tu historia.</p>'),
    ('"The Deep Water"', '"El Agua Profunda"'),
    ('>The Deep Water<', '>El Agua Profunda<'),
    ('"Voice of the Forest"', '"La Voz del Bosque"'),
    ('>Voice of the Forest<', '>La Voz del Bosque<'),
    ('"The Desert Wind"', '"El Viento del Desierto"'),
    ('>The Desert Wind<', '>El Viento del Desierto<'),
    ('"The Hidden Fire"', '"El Fuego Oculto"'),
    ('>The Hidden Fire<', '>El Fuego Oculto<'),
    ('"The Awakening"', '"El Despertar"'),
    ('>The Awakening<', '>El Despertar<'),
    ('"The Star Path"', '"El Camino de las Estrellas"'),
    ('>The Star Path<', '>El Camino de las Estrellas<'),
    ('"The Inner Journey"', '"El Viaje Interior"'),
    ('>The Inner Journey<', '>El Viaje Interior<'),
    ('"The Ancient One"', '"El Ancestral"'),
    ('>The Ancient One<', '>El Ancestral<'),
    ('"Dance of the Sun"', '"La Danza del Sol"'),
    ('>Dance of the Sun<', '>La Danza del Sol<'),
    ('"The Stone Temple"', '"El Templo de Piedra"'),
    ('>The Stone Temple<', '>El Templo de Piedra<'),
    ('<p>The most beloved handpan scale in the world. Deep, meditative, and grounding — like the still waters of a cenote at dawn.</p>',
     '<p>La escala de handpan más querida del mundo. Profunda, meditativa y enraizante, como las aguas quietas de un cenote al amanecer.</p>'),
    ('<p>Warm and flowing, with a natural elegance that evokes the breath of wind through ancient trees.</p>',
     '<p>Cálida y fluida, con una elegancia natural que evoca el soplo del viento entre árboles antiguos.</p>'),
    ('<p>Mysterious and intense. A scale of longing and beauty, carrying the spirit of desert nights.</p>',
     '<p>Misteriosa e intensa. Una escala de anhelo y belleza que lleva el espíritu de las noches del desierto.</p>'),
    ('<p>Tribal, earthy, and rhythmic. Awakens something primal — the heartbeat beneath the surface.</p>',
     '<p>Tribal, terrenal y rítmica. Despierta algo primitivo: el latido bajo la superficie.</p>'),
    ('<p>Bright and uplifting, with a unique character that balances joy and deep introspection.</p>',
     '<p>Luminosa y edificante, con un carácter único que equilibra la alegría y la introspección profunda.</p>'),
    ("<p>Open, expansive, and luminous — like following the Sak Be', the Milky Way road of the Maya.</p>",
     "<p>Abierta, expansiva y luminosa, como seguir el Sak Be', el camino de la Vía Láctea de los mayas.</p>"),
    ('<p>Deeply introspective and emotionally rich. A mirror for the soul — look inward and listen.</p>',
     '<p>Profundamente introspectiva y emocionalmente rica. Un espejo del alma: mira hacia dentro y escucha.</p>'),
    ('<p>Haunting and beautiful, with deep roots in Eastern European musical tradition.</p>',
     '<p>Evocadora y hermosa, con raíces profundas en la tradición musical de Europa del Este.</p>'),
    ('<p>Bright and warm with a playful edge. Golden sunlight made sound.</p>',
     '<p>Luminosa y cálida, con un toque juguetón. Luz dorada del sol hecha sonido.</p>'),
    ('<p>The natural minor scale — pure, timeless, and deeply moving. Like walking through an ancient ruin.</p>',
     '<p>La escala menor natural: pura, atemporal y profundamente conmovedora. Como caminar entre una ruina antigua.</p>'),
    ('<div class="play-hint">Click to play ▸</div>', '<div class="play-hint">Clic para tocar ▸</div>'),
    ('Instruments are available by request or personal visit in Tulum.<br>',
     'Los instrumentos están disponibles por pedido o en visita personal en Tulum.<br>'),
    ('Each handpan is built to order with care and intention.',
     'Cada handpan se fabrica sobre pedido, con cuidado e intención.'),
    ('class="btn" style="margin-top:20px">Request an Instrument</a>',
     'class="btn" style="margin-top:20px">Solicita un instrumento</a>'),

    # --- player ---
    ('<h2 class="section-title">Explore the Sound</h2>', '<h2 class="section-title">Explora el sonido</h2>'),
    ('<p class="section-subtitle">Select a scale and tap the tones to feel the vibration</p>',
     '<p class="section-subtitle">Elige una escala y toca los tonos para sentir la vibración</p>'),
    ('id="btn-play-all">Play Scale ▸</button>', 'id="btn-play-all">Tocar escala ▸</button>'),
    ('<p class="player-hint">Use keys 1-9 to play · Tap or click the tone fields</p>',
     '<p class="player-hint">Usa las teclas 1-9 para tocar · Toca o haz clic en los campos de tono</p>'),

    # --- knowledge ---
    ('<h2 class="section-title">The Knowledge</h2>', '<h2 class="section-title">El conocimiento</h2>'),
    ('<p class="section-subtitle">Understanding the instrument, the sound, and the journey</p>',
     '<p class="section-subtitle">Entender el instrumento, el sonido y el camino</p>'),
    ('<h3>What Is a Handpan?</h3>', '<h3>¿Qué es un handpan?</h3>'),
    ('<p>The handpan is a steel percussion instrument played with the hands. Created in the early 2000s, it belongs to a family of instruments known as steelpans, yet it stands apart in both sound and philosophy. Where the traditional steelpan is loud and festive, the handpan is intimate and meditative.</p>',
     '<p>El handpan es un instrumento de percusión de acero que se toca con las manos. Creado a principios de los años 2000, pertenece a la familia de los steelpans, pero se distingue tanto en sonido como en filosofía. Mientras el steelpan tradicional es fuerte y festivo, el handpan es íntimo y meditativo.</p>'),
    ('<p>A handpan consists of two steel half-shells bonded together. The top surface features a central dome called the "Ding" surrounded by tone fields arranged in a circle. Each tone field is tuned to a specific note, creating a complete musical scale. When struck gently with the fingers or palm, these tone fields produce rich, resonant tones with multiple harmonics.</p>',
     '<p>Un handpan está formado por dos medias esferas de acero unidas. La cara superior tiene una cúpula central llamada "Ding", rodeada de campos de tono dispuestos en círculo. Cada campo de tono está afinado en una nota específica, formando una escala musical completa. Al golpearlos suavemente con los dedos o la palma, producen tonos ricos y resonantes con múltiples armónicos.</p>'),
    ('<p>The most common configuration is 9 notes: one Ding (the bass note at the center) plus 8 surrounding tone fields. This offers enough range for expressive playing while remaining intuitive for beginners. No musical training is required — the scales are designed so that every combination of notes sounds harmonious.</p>',
     '<p>La configuración más común es de 9 notas: un Ding (la nota grave del centro) más 8 campos de tono alrededor. Esto ofrece suficiente rango para tocar con expresión y sigue siendo intuitivo para principiantes. No se necesita formación musical: las escalas están diseñadas para que cualquier combinación de notas suene armoniosa.</p>'),
    ('<h3>Sacred Geometry in Sound</h3>', '<h3>Geometría sagrada en el sonido</h3>'),
    ('<p>The ancient Maya understood that the universe speaks in patterns. Their pyramids, calendars, and temples all follow precise mathematical relationships that mirror the patterns found in nature. The handpan, though a modern creation, embodies this same principle.</p>',
     '<p>Los antiguos mayas entendían que el universo habla en patrones. Sus pirámides, calendarios y templos siguen relaciones matemáticas precisas que reflejan los patrones de la naturaleza. El handpan, aunque es una creación moderna, encarna este mismo principio.</p>'),
    ("<p>Each tone field on a handpan is tuned not just to a fundamental pitch, but to a series of harmonics — the octave and the fifth above. This creates the instrument's characteristic shimmering, bell-like quality. These harmonic ratios — 1:2:3 — are the same proportions found in seashells, galaxies, and the geometry of living things.</p>",
     '<p>Cada campo de tono de un handpan está afinado no solo en una nota fundamental, sino en una serie de armónicos: la octava y la quinta superior. Esto crea la cualidad brillante, como de campana, característica del instrumento. Estas proporciones armónicas (1:2:3) son las mismas que se encuentran en las conchas marinas, las galaxias y la geometría de los seres vivos.</p>'),
    ('<p>When you play a handpan, you are activating a system of resonance where each note contains multitudes, and each combination of notes creates interference patterns that can be felt in the body as much as heard by the ears. This is the same principle the Maya encoded in their architecture: mathematics in service of the sacred.</p>',
     '<p>Cuando tocas un handpan, activas un sistema de resonancia donde cada nota contiene multitudes y cada combinación de notas crea patrones de interferencia que se sienten en el cuerpo tanto como se escuchan. Es el mismo principio que los mayas plasmaron en su arquitectura: las matemáticas al servicio de lo sagrado.</p>'),
    ('<h3>How to Choose Your First Scale</h3>', '<h3>Cómo elegir tu primera escala</h3>'),
    ('<p>Choosing your first handpan scale is less about music theory and more about emotional truth. Each scale carries its own character, its own feeling, its own color. The right scale is the one that moves you.</p>',
     '<p>Elegir tu primera escala de handpan tiene menos que ver con la teoría musical y más con la verdad emocional. Cada escala tiene su propio carácter, su propio sentimiento, su propio color. La escala correcta es la que te conmueve.</p>'),
    ('<p>Minor scales — like D Kurd, D Celtic Minor, and D Aeolian — tend to feel contemplative, emotional, and introspective. They are the most popular for meditation and personal practice. Scales with Eastern influences, like D Hijaz, add tension and mystery. Major and Mixolydian scales feel brighter and more celebratory.</p>',
     '<p>Las escalas menores, como D Kurd, D Celtic Minor y D Aeolian, suelen sentirse contemplativas, emotivas e introspectivas. Son las más populares para la meditación y la práctica personal. Las escalas con influencia oriental, como D Hijaz, añaden tensión y misterio. Las escalas mayores y mixolidias se sienten más luminosas y festivas.</p>'),
    ('<p>If this is your first handpan, the D Kurd 9 is the most versatile and universally loved scale. If you want something with more movement and warmth, try the D Celtic Minor. And if you want to feel something truly unique, explore the E Sabye or D Hijaz. Use the virtual player above to hear each scale, and trust your instincts — the right scale will find you.</p>',
     '<p>Si es tu primer handpan, la D Kurd 9 es la escala más versátil y querida en todo el mundo. Si buscas algo con más movimiento y calidez, prueba la D Celtic Minor. Y si quieres sentir algo realmente único, explora la E Sabye o la D Hijaz. Usa el reproductor virtual de arriba para escuchar cada escala y confía en tu intuición: la escala correcta te encontrará.</p>'),
    ('<h3>The Healing Resonance</h3>', '<h3>La resonancia que sana</h3>'),
    ('<p>Sound has been used for healing since the dawn of human civilization. The Maya used drums, rattles, and voice in ceremonial practices designed to restore balance. Modern science now confirms what these traditions knew: specific sound frequencies can reduce stress, lower blood pressure, and shift brainwave states toward relaxation.</p>',
     '<p>El sonido se ha usado para sanar desde los inicios de la civilización humana. Los mayas usaban tambores, sonajas y la voz en prácticas ceremoniales para restablecer el equilibrio. Hoy la ciencia moderna confirma lo que estas tradiciones sabían: ciertas frecuencias sonoras pueden reducir el estrés, bajar la presión arterial y llevar las ondas cerebrales hacia la relajación.</p>'),
    ('<p>The handpan is uniquely suited for sound therapy. Its rich harmonic overtones create a phenomenon known as "entrainment" — where the listener\'s brainwaves naturally synchronize with the frequencies of the instrument. The sustained resonance of each note acts as a sonic anchor, drawing attention into the present moment.</p>',
     '<p>El handpan es ideal para la terapia de sonido. Sus ricos armónicos crean un fenómeno conocido como "sincronización" (entrainment), en el que las ondas cerebrales de quien escucha se sincronizan de forma natural con las frecuencias del instrumento. La resonancia sostenida de cada nota actúa como un ancla sonora que lleva la atención al momento presente.</p>'),
    ("<p>Many handpan players report entering meditative states effortlessly while playing. This is not accidental — it is a natural consequence of the instrument's harmonic design. The sound wraps around you, and for a few minutes, the noise of the world falls away.</p>",
     '<p>Muchos músicos de handpan cuentan que entran en estados meditativos sin esfuerzo mientras tocan. No es casualidad: es una consecuencia natural del diseño armónico del instrumento. El sonido te envuelve y, por unos minutos, el ruido del mundo desaparece.</p>'),
    ('<h3>Caring for Your Instrument</h3>', '<h3>Cómo cuidar tu instrumento</h3>'),
    ('<p>A handpan is a living instrument. The steel responds to its environment — humidity, temperature, and the oils from your hands all affect its surface and its voice. With proper care, your handpan will last for generations.</p>',
     '<p>Un handpan es un instrumento vivo. El acero responde a su entorno: la humedad, la temperatura y los aceites de tus manos afectan su superficie y su voz. Con el cuidado adecuado, tu handpan durará generaciones.</p>'),
    ('<p>Always clean your handpan after playing. Use a soft microfiber cloth to wipe away fingerprints and moisture. Apply a thin layer of protective oil — Phoenix Oil, Froglube, or coconut oil — every few weeks, or more often in humid or coastal environments. Store your handpan in its case when not in use, and avoid direct sunlight, extreme heat, and high humidity.</p>',
     '<p>Limpia siempre tu handpan después de tocar. Usa un paño suave de microfibra para quitar huellas y humedad. Aplica una capa fina de aceite protector (Phoenix Oil, Froglube o aceite de coco) cada pocas semanas, o más seguido en ambientes húmedos o costeros. Guarda tu handpan en su funda cuando no lo uses y evita la luz directa del sol, el calor extremo y la humedad alta.</p>'),
    ('<p>If you notice any changes in tuning, do not attempt to retune the instrument yourself — contact a professional tuner. Minor tuning drift is normal and can be corrected. With regular care and respect, your SHIVAPAN handpan will continue to sing for a lifetime.</p>',
     '<p>Si notas cambios en la afinación, no intentes reafinar el instrumento tú mismo: contacta a un afinador profesional. Una ligera desafinación es normal y se puede corregir. Con cuidado y respeto, tu handpan SHIVAPAN seguirá cantando toda la vida.</p>'),

    # --- videos ---
    ('<h2 class="section-title">See and Hear</h2>', '<h2 class="section-title">Mira y escucha</h2>'),
    ('<p class="section-subtitle">SHIVAPAN instruments in their element</p>',
     '<p class="section-subtitle">Instrumentos SHIVAPAN en su elemento</p>'),
    ('<span>Video coming soon</span>', '<span>Video próximamente</span>'),

    # --- contact ---
    ('<h2 class="section-title">Begin Your Journey</h2>', '<h2 class="section-title">Comienza tu camino</h2>'),
    ('<p class="section-subtitle">The instrument is not chosen online — it is felt in person</p>',
     '<p class="section-subtitle">El instrumento no se elige en línea: se siente en persona</p>'),
    ('<h3>Reach Us</h3>', '<h3>Contáctanos</h3>'),
    ('<div class="label">Email</div>', '<div class="label">Correo</div>'),
    ('<div class="label">Phone / WhatsApp</div>', '<div class="label">Teléfono / WhatsApp</div>'),
    ('<div class="label">Visit</div>', '<div class="label">Visita</div>'),
    ('Schedule a private visit in Tulum to experience the instruments in person.',
     'Agenda una visita privada en Tulum para conocer los instrumentos en persona.'),
    ('<div class="label">Location</div>', '<div class="label">Ubicación</div>'),
    ('placeholder="Your Name"', 'placeholder="Tu nombre"'),
    ('placeholder="Your Email"', 'placeholder="Tu correo"'),
    ('placeholder="Subject"', 'placeholder="Asunto"'),
    ('placeholder="Tell us about the instrument you\'re looking for, or schedule a visit..."',
     'placeholder="Cuéntanos qué instrumento buscas o agenda una visita..."'),
    ('<button type="submit" class="btn">Send Message</button>', '<button type="submit" class="btn">Enviar mensaje</button>'),

    # --- footer ---
    ('<p>&copy; 2026 SHIVAPAN — Handcrafted in Tulum, México</p>', '<p>&copy; 2026 SHIVAPAN — Hecho a mano en Tulum, México</p>'),
    ('<p class="footer-tagline">Inspired by the cenotes, forged by hand</p>',
     '<p class="footer-tagline">Inspirado en los cenotes, forjado a mano</p>'),

    # --- script messages ---
    ('"Available instrument: "', '"Instrumento disponible: "'),
    ('|| "Handpan Inquiry"', '|| "Consulta de handpan"'),
    ('"SHIVAPAN website: " + subject', '"Sitio SHIVAPAN (ES): " + subject'),
    ('status.textContent = "Sending…";', 'status.textContent = "Enviando…";'),
    ('"Thank you — your message has been sent. We will reply soon."',
     '"Gracias, tu mensaje fue enviado. Te responderemos pronto."'),
    ("'Sorry, the message could not be sent. Please write to us at <a href=\"'",
     "'Lo sentimos, no se pudo enviar el mensaje. Escríbenos a <a href=\"'"),
]


def main():
    html = SRC.read_text(encoding="utf-8")
    missing = []
    for en, es in T:
        if en not in html:
            missing.append(en)
            continue
        html = html.replace(en, es)
    if missing:
        print("English text not found in index.html (update the translation):", file=sys.stderr)
        for m in missing:
            print("  -", m[:120], file=sys.stderr)
        sys.exit(1)
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(T)} translations)")


if __name__ == "__main__":
    main()
