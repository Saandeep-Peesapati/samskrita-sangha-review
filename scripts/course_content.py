"""Original beginner lessons; grammatical references are public-domain Whitney chapters.

All examples deliberately keep word boundaries visible. External sandhi is beyond
this foundation course. Source links and that convention appear on every lesson.
"""
from html import escape

def term(sa, roman, meaning=''):
    return f'<span class="term"><span lang="sa">{escape(sa)}</span> <span class="roman">{escape(roman)}</span>{(" — " + escape(meaning)) if meaning else ""}</span>'

def p(text): return ('p', text)
def note(text): return ('note', text)
def table(caption, headers, rows): return ('table', caption, headers, rows)
def examples(*rows): return ('examples', rows)
def section(title, *blocks): return {'title': title, 'blocks': blocks}
def quiz(question, options, answer, why): return {'question':question, 'options':options, 'answer':answer, 'why':why}
def practice(question, answer): return {'question':question, 'answer':answer}
def lesson(id, title, subtitle, prerequisites, objectives, sections, mistakes, recap, quizzes, exercises, sources):
    return dict(id=id, title=title, subtitle=subtitle, prerequisites=prerequisites, objectives=objectives, sections=sections, mistakes=mistakes, recap=recap, quizzes=quizzes, exercises=exercises, sources=sources)

LESSONS = [
lesson('sounds', 'Sounds & the Sanskrit alphabet', 'Hear the distinctions that make words different.', [],
 ['Recognise short and long vowels.', 'Distinguish dental, retroflex, and aspirated consonants.', 'Use IAST as a guide while learning the script.'], [
 section('Start with sounds, not English spelling',
 p('Sanskrit spelling makes distinctions that English spelling often hides. A long vowel and a short vowel are different sounds; a consonant with a puff of breath and one without it are different consonants. You do not need to memorise the whole alphabet today. Begin by noticing these contrasts and reading the examples slowly.'),
 p('Every lesson gives the Sanskrit script, a matching IAST transliteration, and an English meaning. IAST uses Roman letters with marks: a line above a vowel indicates length, and dots below certain letters distinguish sounds. Transliteration records the Sanskrit spelling; it is not an English translation or a perfect substitute for hearing a teacher.')),
 section('Give long vowels more time',
 p('Practise a short vowel for one beat and its long partner for approximately two. Keep the vowel steady rather than turning it into an English glide. The first three pairs are the most useful place to begin.'),
 table('Three everyday short–long pairs', ['Short','Long','What changes?'], [
 [term('अ','a'),term('आ','ā'),'Length'],[term('इ','i'),term('ई','ī'),'Length'],[term('उ','u'),term('ऊ','ū'),'Length']]),
 p('The wider inventory includes '+term('ऋ','ṛ')+' and its rare long partner '+term('ॠ','ṝ')+', the rare '+term('ऌ','ḷ')+', and '+term('ए ऐ ओ औ','e ai o au')+'. The last four count as long vowels. Syllabic ṛ is itself a vowel; do not routinely insert a full i after r. Learn the common six vowels first, then recognise the others as they occur.'),
 examples(('बलम्','balam','Strength. Notice the short a.','A noun used as a sound comparison.'),('बालः','bālaḥ','Boy. Notice the long ā.','The long mark changes the sound; these words have different meanings.'))),
 section('The consonants have an orderly map',
 p('The five stop-consonant rows move from the back of the mouth towards the lips. Within each row, the second and fourth sounds are aspirated: they include a release of breath. For example, kh is one aspirated consonant, not the two syllables ka-ha. The dental t touches the teeth; retroflex ṭ uses the tongue turned back towards the roof of the mouth.'),
 table('Five rows of consonants (with inherent a for practice)', ['Place','Devanagari','IAST'],[
 ['Back of mouth','क ख ग घ ङ','ka kha ga gha ṅa'],['Palate','च छ ज झ ञ','ca cha ja jha ña'],['Retroflex','ट ठ ड ढ ण','ṭa ṭha ḍa ḍha ṇa'],['Teeth','त थ द ध न','ta tha da dha na'],['Lips','प फ ब भ म','pa pha ba bha ma']]),
 p('The remaining consonants are '+term('य र ल व','ya ra la va')+', '+term('श ष स','śa ṣa sa')+', and '+term('ह','ha')+'. In IAST, c is a single consonant like the opening sound of “church”; th is an aspirated t, not English “th” in “think”. Text descriptions are approximate: a teacher can help refine tongue position.')),
 section('Two signs you will meet immediately',
 p(term('ं','ṃ','anusvāra')+' marks a nasal sound whose realisation depends on its context. '+term('ः','ḥ','visarga')+' marks a breath sound after a vowel. Neither is simply decorative punctuation. A full lesson on how sounds change between words comes later, outside this foundation tree.'),
 p('For a two-minute practice, read the three short–long pairs aloud three times. Then alternate ka and kha, ta and ṭa. Finish by identifying the long vowels in bālaḥ and mālā. Success here means noticing the distinctions, not producing every sound perfectly on the first attempt.'))
 ], ['Do not pronounce ā, ī, and ū as ordinary short vowels.', 'Do not read th as English “th” or treat ḥ as punctuation.'],
 ['Length matters.', 'Consonant rows organise place and breath.', 'IAST preserves distinctions while you learn Devanagari.'],
 [quiz('Which vowel is long?', ['इ — i','ई — ī','अ — a'],1,'The macron in ī marks a long vowel; इ i is its short partner.'),quiz('How is ख — kha different from क — ka?', ['It is aspirated, with a puff of breath','It is a long vowel','It has no vowel'],0,'The kh consonant is aspirated. Both written forms here include a.'),quiz('What does the dot in ṭ help distinguish?', ['Plural number','A long vowel','A retroflex consonant'],2,'IAST ṭ is retroflex; t without the dot is dental.')],
 [practice('Write the long partners of अ a, इ i, and उ u.',term('आ ई ऊ','ā ī ū')+'. Hold each vowel longer.'),practice('Read बालः bālaḥ. Identify the long vowel and final sign.','The long vowel is '+term('आ','ā')+'. The final sign is '+term('ः','ḥ','visarga')+'. The word means “boy”.')], ['I','II']),

lesson('script','Read your first words','Connect consonants, vowel marks, and syllables.', ['sounds'],
 ['Read consonants with and without a vowel.', 'Recognise common dependent vowel marks.', 'Break a short written word into sound units.'], [
 section('A consonant normally includes a',
 p('Devanagari is built around syllables. The ordinary consonant letter '+term('क','ka')+' includes the vowel a unless another sign changes it. To write just the consonant k, use '+term('क्','k')+'. The small mark underneath is the virāma: it cancels the inherent vowel. This is why reading Sanskrit as a collection of English-style letters can produce extra or missing vowels.'),
 p('An independent vowel letter is used when a vowel begins a syllable without a preceding consonant. A vowel following a consonant usually appears as a dependent mark, often called a mātrā. These are two ways to represent a vowel, not two different vowel sounds.')),
 section('One consonant, several vowel marks',
 table('Read these from the sound, not the mark’s position', ['Vowel','With क','IAST'],[
 ['अ a','क','ka'],['आ ā','का','kā'],['इ i','कि','ki'],['ई ī','की','kī'],['उ u','कु','ku'],['ऊ ū','कू','kū'],['ऋ ṛ','कृ','kṛ'],['ए e','के','ke'],['ऐ ai','कै','kai'],['ओ o','को','ko'],['औ au','कौ','kau']]),
 p('In '+term('कि','ki')+', the i mark is printed to the left of the consonant, but you still pronounce k before i. In '+term('कु','ku')+' and '+term('कू','kū')+', look below the consonant. When handwriting, pay attention to which consonant each mark belongs to; the horizontal headline can make several syllables look like one unit.'),
 p('The same principle works with other consonants: '+term('प पा पि पी पु पू','pa pā pi pī pu pū')+'. Read each series aloud, then cover the Roman letters and try again.')),
 section('Join consonants without inserting vowels',
 p('Two adjacent consonants without a vowel between them form a cluster. They may appear as a combined shape or as a reduced letter joined to the next. For instance, '+term('क्त','kta')+' combines k and t before a; it does not mean kata. In '+term('पुस्तकम्','pustakam','book')+', the cluster st occurs between pu and ka.'),
 examples(('पठति','paṭhati','He, she, or it reads.','Read pa + ṭha + ti. The ṭh is one aspirated consonant.'),('फलम्','phalam','Fruit.','Read pha + lam. Final म् has no following a.'),('पुस्तकम्','pustakam','Book.','Read pus + ta + kam. Do not add a vowel between s and t.')),
 p('At a word’s end, '+term('म्','m')+' is a consonant without a vowel. You will also meet a dot above the line, '+term('ं','ṃ')+', especially before another consonant. This course shows isolated noun forms with final m and often uses ṃ before consonants in sentences. The transliteration always matches the displayed spelling.')),
 section('A repeatable reading routine',
 p('First find the vowels and vowel marks. Next check for a virāma or joined consonants. Then read from left to right in syllables. Finally compare the IAST and the meaning. This is a reading routine, not a demand to understand every grammatical ending immediately.'),
 p('The sign '+term('।','daṇḍa')+' closes a sentence or a verse segment. It is not spoken as a sound. Read '+term('अहं पठामि।','ahaṃ paṭhāmi.','I read.')+' slowly: a-haṃ, pa-ṭhā-mi. Notice both the nasal sign and the long ā. Spend a minute copying the sentence, then point to each mark and say what it does.'))
 ], ['A mark printed before a consonant need not be pronounced first: कि is ki.', 'Final म् is m, not ma.', 'Do not add vowels inside consonant clusters.'],
 ['A plain consonant includes a.', 'A vowel mark changes that vowel; virāma removes it.', 'Read clusters and final consonants carefully.'],
 [quiz('How do you read कि?', ['ik','ki','kī'],1,'The i mark is written on the left but pronounced after k.'),quiz('What does the virāma in क् do?', ['Adds a long vowel','Makes the word plural','Removes the inherent a'],2,'क् represents k without a following vowel.'),quiz('Which spelling is kā?', ['का','क','कि'],0,'The ा sign supplies long ā.')],
 [practice('Write ka, ki, and kū in Devanagari.',term('क कि कू','ka ki kū')+'. The marks distinguish a, i, and long ū.'),practice('Why does फलम् phalam not end in ma?','The virāma under the final '+term('म्','m')+' removes a. '+term('फलम्','phalam')+' means “fruit”.')], ['I']),

lesson('sentence-parts','Words & simple sentences','Find who acts, what happens, and what is involved.', ['script'],
 ['Recognise a noun, a pronoun, and a verb.', 'Find the subject and direct object in a simple sentence.', 'Use endings as clues instead of relying only on word order.'], [
 section('Begin with a small complete thought',
 examples(('बालः पठति।','bālaḥ paṭhati.','The boy reads.','बालः names the subject; पठति gives the action.'),('बालिका लिखति।','bālikā likhati.','The girl writes.','The subject changes, but the third-person singular verb still ends in -ti.')),
 p('A sentence tells us something. In these examples, a noun names a person and a verb tells what that person does. A noun can also name an object, a place, or an idea. A pronoun such as “I” or “she” can stand in for a noun. You will learn their forms later; for now, identify the job each word is doing.'),
 p('Sanskrit has no separate articles corresponding exactly to English “a”, “an”, and “the”. Depending on context, bālaḥ can mean “a boy” or “the boy”. Our English translations choose whichever reads naturally. Do not search for a hidden Sanskrit word for every English article.')),
 section('Ask three useful questions',
 p('First ask: what is happening? That locates the verb. Next ask: who or what is doing it? That locates the subject in our active examples. Finally ask whether the action directly affects someone or something. That may identify a direct object. Not every sentence needs one: “The boy plays” is already complete.'),
 examples(('बालिका पुस्तकं पठति।','bālikā pustakaṃ paṭhati.','The girl reads a book.','What happens? Reading. Who reads? The girl. What is read? A book.'),('बालः क्रीडति।','bālaḥ krīḍati.','The boy plays.','This sentence does not require a direct object.')),
 table('A small working vocabulary', ['Sanskrit & IAST','Meaning','Kind'],[
 [term('बालः','bālaḥ'),'boy','Noun'],[term('बालिका','bālikā'),'girl','Noun'],[term('पुस्तकम्','pustakam'),'book','Noun'],[term('पठति','paṭhati'),'reads / is reading','Verb'],[term('लिखति','likhati'),'writes / is writing','Verb'],[term('क्रीडति','krīḍati'),'plays / is playing','Verb']]),
 p('Learn a word together with its meaning, then use it in a small thought. Looking only at isolated vocabulary will not teach you how the words cooperate. Cover the translation of the book example and identify its three jobs before translating.')),
 section('Endings carry information',
 p('English uses word order heavily to distinguish “the boy sees the girl” from “the girl sees the boy”. Sanskrit commonly marks roles through word endings. Changing an ending may change who acts or who receives the action. These changes are called inflection. Noun inflection is declension; verb inflection is conjugation.'),
 p('A dictionary stem is the base used to organise a noun’s forms. '+term('बाल','bāla')+' is a stem; '+term('बालः','bālaḥ')+' is a form suitable for the subject of a singular active sentence. Do not assume that the stem by itself is always a complete sentence word. The next lessons explain which ending to choose.'),
 note('Examples in this course keep words separate and sometimes retain their pause forms. Sound changes between words, called external sandhi, are intentionally postponed. This lets you see each grammatical form clearly.')),
 section('Build one sentence, then change one part',
 p('A useful beginner order is subject → object, if needed → verb. Sanskrit word order is flexible, but this pattern keeps practice manageable. Start with “The girl reads a book”. Change “reads” to “writes” and you have a new sentence while retaining the same broad structure. Change only the subject and check that the verb still agrees with it.'),
 p('For now, use the supplied singular forms rather than inventing endings. In the final lesson you will construct sentences independently. Before moving on, explain in your own words why “book” is an object in the reading sentence, while “boy” is a subject in the playing sentence.'))
 ], ['Do not equate the first word with the subject in every Sanskrit sentence.', 'A dictionary stem and a complete inflected word are not always identical.', 'Not every verb needs a direct object.'],
 ['Find the action, then its subject and any object.', 'Nouns name; verbs tell actions or states; pronouns stand in for nouns.', 'Endings help identify grammatical roles.'],
 [quiz('In बालिका पुस्तकं पठति। — bālikā pustakaṃ paṭhati, what is being read?', ['The girl','The book','The verb ending'],1,'Pustakaṃ is the book, the direct object of reading.'),quiz('Which word is a verb?', ['पुस्तकम् — pustakam','बालिका — bālikā','लिखति — likhati'],2,'Likhati means “writes” or “is writing”.'),quiz('Which beginner word order will we usually practise?', ['Subject → object → verb','Always verb → subject → object','Alphabetical order'],0,'Subject–object–verb is a useful practice pattern, though actual Sanskrit word order is flexible.')],
 [practice('Identify the subject and verb in बालः क्रीडति। — bālaḥ krīḍati.','Subject: '+term('बालः','bālaḥ','the boy')+'. Verb: '+term('क्रीडति','krīḍati','plays')+'. There is no direct object.'),practice('Replace “reads” with “writes” in “The girl reads a book”.',term('बालिका पुस्तकं लिखति।','bālikā pustakaṃ likhati.','The girl writes a book.')+' The action changes; the subject and object remain.')], ['IV','IX']),

lesson('gender','Grammatical gender','Learn the three noun classes without guessing from meaning.', ['sentence-parts'],
 ['Recognise masculine, feminine, and neuter.', 'Learn a noun with its gender and stem.', 'Understand how an adjective matches the noun it describes.'], [
 section('Gender is a grammatical classification',
 p('Sanskrit nouns belong to three genders: masculine, feminine, and neuter. These are grammatical classes. A noun naming a male or female person often follows natural gender, but many nouns name things or ideas, and their gender must be learned. Neuter does not mean that a word is unimportant, and masculine does not mean that the object is alive.'),
 table('Learn meaning and gender together', ['Stem','Gender','Subject form: one'],[
 [term('बाल','bāla','boy'),'Masculine',term('बालः','bālaḥ')],[term('वृक्ष','vṛkṣa','tree'),'Masculine',term('वृक्षः','vṛkṣaḥ')],[term('बालिका','bālikā','girl'),'Feminine',term('बालिका','bālikā')],[term('लता','latā','creeper'),'Feminine',term('लता','latā')],[term('फल','phala','fruit'),'Neuter',term('फलम्','phalam')],[term('पुस्तक','pustaka','book'),'Neuter',term('पुस्तकम्','pustakam')]]),
 p('The distinction between stem and sentence form matters here. Bāla and phala both have stems ending in short a, yet they belong to different genders. Their singular subject forms end differently: bālaḥ and phalam. Gender helps you choose the right pattern of endings.')),
 section('Useful clues are not universal rules',
 p('Many masculine nouns have stems in short a, many feminine nouns have stems in long ā, and many neuter nouns have stems in short a. These three common groups form the branches of our noun lessons. They are a good beginning, but Sanskrit has other endings and irregular patterns.'),
 p('For example, '+term('नदी','nadī','river')+' is feminine although it ends in ī, not ā. We will recognise it as an illustration rather than learn its full declension in this course. A dictionary entry or a reliable vocabulary list is a safer guide to gender than the final letter alone.'),
 note('Make a vocabulary card with three pieces of information: stem, meaning, and gender. Add a model form when useful: phala — fruit — neuter; singular subject phalam.')),
 section('Describing words agree with nouns',
 p('An adjective describes a noun. Its form usually agrees with that noun in gender, number, and case. Think of the adjective and noun as a pair whose grammatical labels must match. This does not mean that their final letters must always be identical, since different kinds of stems use different patterns.'),
 examples(('सुन्दरः बालः','sundaraḥ bālaḥ','A beautiful boy.','Both words are masculine, singular, and nominative.'),('सुन्दरा बालिका','sundarā bālikā','A beautiful girl.','Both words are feminine, singular, and nominative.'),('सुन्दरं फलम्','sundaraṃ phalam','A beautiful fruit.','Both words are neuter, singular, and nominative. The adjective is written with ṃ before ph.')),
 p('The stem sundara is used here in its masculine and neuter patterns; its feminine stem is sundarā. Other adjectives can form their feminine differently. Learn this one model now, without trying to make every Sanskrit adjective follow it.')),
 section('Gender and ordinary present-tense verbs',
 p('In the active present-tense forms used in this course, the verb changes for person and number, not for the gender of its subject. Thus a boy and a girl can both be described with paṭhati. This is different from the agreement of an adjective, and from some verbal adjective constructions studied later.'),
 examples(('बालः पठति।','bālaḥ paṭhati.','The boy reads.','Masculine subject; third-person singular verb.'),('बालिका पठति।','bālikā paṭhati.','The girl reads.','Feminine subject; the same third-person singular verb.')),
 p('Practise by sorting the six nouns above into three groups. Then choose the appropriate form of sundara for one noun from each group. Say the gender aloud as you make each choice; you are training a grammatical habit, not merely memorising a word ending.'))
 ], ['Do not assume all objects are neuter: vṛkṣa, “tree”, is masculine.', 'Final ā is a useful clue in our model, not a complete rule for all nouns.', 'Do not change paṭhati just because a singular subject is feminine.'],
 ['Sanskrit has three grammatical genders.', 'Learn gender with each noun.', 'Adjectives agree in gender, number, and case.'],
 [quiz('What is the gender of पुस्तक — pustaka, “book”?', ['Masculine','Feminine','Neuter'],2,'Pustaka is a neuter noun; its singular nominative is pustakam.'),quiz('Which description matches बालिका — bālikā?', ['सुन्दरा — sundarā','सुन्दरः — sundaraḥ','सुन्दरम् — sundaram'],0,'The feminine singular nominative adjective is sundarā.'),quiz('What happens to paṭhati when bālaḥ is replaced by bālikā?', ['It must become paṭhāmi','It remains paṭhati','It must become plural'],1,'These present-tense verbs agree with person and number, not gender.')],
 [practice('Why can you not classify every short-a stem as masculine?','Both '+term('बाल','bāla','boy')+' and '+term('फल','phala','fruit')+' end in a. Bāla is masculine and phala is neuter.'),practice('Choose a matching adjective for “a beautiful creeper”.',term('सुन्दरा लता','sundarā latā','a beautiful creeper')+'. Both words are feminine singular nominative.')], ['IV','V']),

lesson('number','One, two & many','Use singular, dual, and plural deliberately.', ['sentence-parts'],
 ['Distinguish singular, dual, and plural.', 'Recognise number in basic subject forms.', 'Match a third-person verb to its subject’s number.'], [
 section('Exactly two has its own form',
 p('Sanskrit distinguishes one, exactly two, and more than two. The names are singular, dual, and plural. English usually groups two and three together as plural; Sanskrit does not. When you mean exactly two boys, you normally choose the dual noun and a dual verb.'),
 table('Three numbers in subject forms', ['Model','One','Exactly two','Three or more'],[
 ['Boy',term('बालः','bālaḥ'),term('बालौ','bālau'),term('बालाः','bālāḥ')],['Girl',term('बालिका','bālikā'),term('बालिके','bālike'),term('बालिकाः','bālikāḥ')],['Fruit',term('फलम्','phalam'),term('फले','phale'),term('फलानि','phalāni')]]),
 p('These are nominative forms: forms suitable for the subject. You do not obtain every plural by adding a single universal suffix to the singular. Each stem type has a pattern, and different cases can use different endings. The noun branches later in the tree develop these models.')),
 section('The subject and verb work as a pair',
 p('A third-person subject is someone or something other than the speaker “I” or the listener “you”. In our present-tense reading model, use paṭhati for one, paṭhataḥ for two, and paṭhanti for more than two. The noun ending and verb ending together tell you the number.'),
 examples(('बालः पठति।','bālaḥ paṭhati.','The boy reads.','One subject: singular noun and singular verb.'),('बालौ पठतः।','bālau paṭhataḥ.','The two boys read.','Exactly two: dual noun and dual verb.'),('बालाः पठन्ति।','bālāḥ paṭhanti.','The boys read.','More than two: plural noun and plural verb.')),
 p('Read each sentence aloud and point first to the noun ending, then to the verb ending. The final ḥ in paṭhataḥ belongs to the verb form; it does not turn the verb into a noun. Endings must be understood as part of a pattern, rather than assigned a single meaning everywhere.')),
 section('Count the subject, not the nearby object',
 p('The verb agrees with its subject, even when the object has another number. One girl may read several books. Several girls may read one book. The number of books does not control the verb because the books are not the subject of these active sentences.'),
 examples(('बालिका पुस्तकानि पठति।','bālikā pustakāni paṭhati.','The girl reads books.','One girl controls singular paṭhati; pustakāni is a plural object.'),('बालिकाः पुस्तकं पठन्ति।','bālikāḥ pustakaṃ paṭhanti.','The girls read a book.','The plural subject controls paṭhanti, even though the object is singular.')),
 p('This is a useful way to diagnose mistakes. If a sentence has a plural object, do not immediately choose a plural verb. First locate the subject and count it. Then return to the object and give it its own appropriate form.')),
 section('Practise one change at a time',
 p('Start with bālaḥ paṭhati. Change the meaning to “two boys read”; change both words, not just the noun. Next make it “the boys read”. Finally use the feminine noun forms from the table with the same three verbs. Since the verb forms here do not change for gender, the number pattern stays familiar.'),
 p('You do not have to add a numeral meaning “two” whenever you use a dual. The dual ending already signals two. Numerals have their own grammar, which lies outside this small foundation course. Today’s goal is to make one/two/many an automatic question whenever you choose a noun or verb form.'))
 ], ['Dual means exactly two; plural normally means more than two.', 'Changing the subject’s number usually also requires changing the verb.', 'A plural object does not by itself require a plural verb.'],
 ['There are three numbers.', 'Subject and verb agree in number.', 'Nouns of different patterns have different number endings.'],
 [quiz('Which number is used for exactly two?', ['Singular','Dual','Plural'],1,'The dual is the ordinary form for exactly two.'),quiz('Complete बालौ … — bālau … (“The two boys read”).', ['पठति — paṭhati','पठन्ति — paṭhanti','पठतः — paṭhataḥ'],2,'A dual subject takes the third-person dual form paṭhataḥ.'),quiz('In “The girl reads books”, what determines the verb’s number?', ['The one girl','The many books','The number of words'],0,'The subject, the girl, is singular.')],
 [practice('Change बालिका पठति। — bālikā paṭhati to “The two girls read”.',term('बालिके पठतः।','bālike paṭhataḥ.','The two girls read.')+' Both subject and verb become dual.'),practice('Translate बालाः पुस्तकं पठन्ति। — bālāḥ pustakaṃ paṭhanti.', 'The boys read a book. The subject is plural; the direct object is singular.')], ['IV','V','IX']),

lesson('cases','The eight case roles','Choose a form by the job a noun does.', ['gender','number'],
 ['Recognise the common job of each case.', 'Distinguish a subject, object, possessor, and location.', 'Use context when two case forms look alike.'], [
 section('A case connects a noun to the sentence',
 p('A case is a grammatical form that helps express how a noun relates to other words. In English, a preposition such as “with”, “from”, or “in” often does this work. Sanskrit frequently uses an ending instead. A noun’s form also reflects number and its declension pattern, so case is one part of a larger decision.'),
 p('Begin with two questions you already know: who acts, and what is directly affected? In our simple active sentences, the subject is nominative and the direct object is accusative. Other cases let us add an instrument, a recipient, a starting point, a possessor, or a location.'),
 note('We teach seven numbered cases plus the vocative, a form used for addressing someone. “Eight cases” is convenient beginner shorthand; the traditional system treats the vocative as address associated with the first case.')),
 section('Eight useful questions',
 table('Core meanings, using the masculine stem bāla (boy)', ['Case','Useful question','One boy: form and typical sense'],[
 ['1 · Nominative','Who acts?',term('बालः','bālaḥ','the boy, as subject')],['2 · Accusative','Whom / what directly?',term('बालम्','bālam','the boy, as object')],['3 · Instrumental','By / with what?',term('बालेन','bālena','by or with the boy')],['4 · Dative','To / for whom?',term('बालाय','bālāya','to or for the boy')],['5 · Ablative','From whom / what?',term('बालात्','bālāt','from the boy')],['6 · Genitive','Whose?',term('बालस्य','bālasya','of the boy')],['7 · Locative','In / on / at what?',term('बाले','bāle','in or on the boy')],['Vocative','Whom am I addressing?',term('बाल','bāla','O boy!')]]),
 p('The questions are starting points, not word-for-word translation laws. A verb or a construction can require a case for reasons that an English preposition does not predict. For example, an accusative can also indicate a destination with some motion verbs. Learn the central meanings now and check unfamiliar constructions later.')),
 section('See cases in small, understandable pieces',
 examples(('बालिका पुस्तकं पठति।','bālikā pustakaṃ paṭhati.','The girl reads a book.','Bālikā is nominative; pustakaṃ is accusative.'),('बालस्य पुस्तकम्','bālasya pustakam','The boy’s book.','Bālasya is genitive. This is a phrase, not a complete action sentence.'),('बालिका ग्रामे वसति।','bālikā grāme vasati.','The girl lives in the village.','Grāme is locative of grāma, “village”.'),('बालिका लेखन्या लिखति।','bālikā lekhanyā likhati.','The girl writes with a pen.','Lekhanī means “pen”; lekhanyā is its instrumental. Its full stem pattern is outside this course.')),
 p('Notice that these forms cannot be built by attaching the same letters to every noun. Bālena and lekhanyā both express an instrumental role but belong to different stem patterns. This lesson explains the jobs; the next three lessons explain common sets of forms.')),
 section('One form can have more than one job',
 p('A form does not always identify its case uniquely. Neuter nouns have the same nominative and accusative forms in each number. Some feminine singular forms also share endings across cases. Context, the verb, and the other words help you decide which role is intended.'),
 p('Use a four-step routine: identify the meaning, identify the role, decide the number, and choose the form from the correct noun pattern. For “the boy’s book”, the boy is the possessor: choose genitive singular bālasya. The book has its own role in the larger sentence; the possessor does not determine the book’s case.'),
 p('Spend a minute giving an English phrase for each case before memorising endings. Being able to say why a word needs a genitive or a locative is more useful than reciting a table without understanding it.'))
 ], ['Do not translate every English “to” automatically with the dative.', 'Case and number are separate decisions.', 'A repeated form may express different cases; use context.'],
 ['Cases express relationships.', 'Nominative marks the subject and accusative the direct object in our active examples.', 'Genitive often marks possession; locative often marks location.'],
 [quiz('Which case expresses “of the boy” in बालस्य — bālasya?', ['Genitive','Accusative','Vocative'],0,'The genitive commonly expresses possession or a relationship: “of the boy”.'),quiz('Which case normally marks the direct object of “reads”?', ['Locative','Accusative','Ablative'],1,'What is read is the direct object, normally in the accusative.'),quiz('Which role does ग्रामे — grāme have in “The girl lives in the village”?', ['The person addressed','The direct object','The location'],2,'Grāme is locative singular: “in the village”.')],
 [practice('Choose cases for “the girl”, “a book”, and “in the village” in “The girl reads a book in the village”.','The girl: nominative. A book: accusative. In the village: locative. The subject, object, and location have different roles.'),practice('Explain why बालस्य पुस्तकम् — bālasya pustakam means “the boy’s book”.',term('बालस्य','bālasya')+' is genitive singular, marking the possessor. '+term('पुस्तकम्','pustakam')+' is “book”; the phrase alone does not tell whether the book is a subject or object in a larger sentence.')], ['IV']),
]

LESSONS += [
lesson('masculine-a','Masculine nouns in a','Use bāla, “boy”, as a model for common noun forms.', ['cases'],
 ['Distinguish a short-a stem from its sentence forms.', 'Use the eight singular forms of bāla.', 'Recognise subject and object forms in all three numbers.'], [
 section('Choose a model before choosing an ending',
 p('A declension pattern is a family of forms used by nouns with a particular kind of stem. Here our model is masculine '+term('बाल','bāla','boy')+'. The final short a belongs to the stem. The singular subject is bālaḥ, while the singular object is bālam. A noun is still the same noun when its form changes; the form tells you how it works in a sentence.'),
 p('Other useful masculine a-stems include '+term('देव','deva','god')+', '+term('ग्राम','grāma','village')+', and '+term('वृक्ष','vṛkṣa','tree')+'. This lesson covers the singular case set plus the subject and object forms for two and many. You can begin forming sentences without learning every possible noun paradigm at once.')),
 section('Eight singular forms, eight jobs',
 table('Masculine bāla: singular', ['Case','Form','Typical sense'],[
 ['Nominative',term('बालः','bālaḥ'),'the boy as subject'],['Accusative',term('बालम्','bālam'),'the boy as object'],['Instrumental',term('बालेन','bālena'),'by / with the boy'],['Dative',term('बालाय','bālāya'),'to / for the boy'],['Ablative',term('बालात्','bālāt'),'from the boy'],['Genitive',term('बालस्य','bālasya'),'of the boy'],['Locative',term('बाले','bāle'),'in / on the boy'],['Vocative',term('बाल','bāla'),'O boy!']]),
 p('Treat each row as a meaningful unit. To express possession, say bālasya and “of the boy” together. To address the boy, use bāla rather than the subject form bālaḥ. Repeating forms with their jobs is more effective than learning eight sounds without context.'),
 p('The visible result is not always made by simply adding letters after the dictionary form. The final vowel can change or combine with an ending: bāla becomes bāle in the locative. Learn the finished model forms first; detailed sound rules can be studied after the foundation course.')),
 section('Subject and object: one, two, many',
 table('The most useful number contrast', ['Role','One','Two','Many'],[
 ['Subject',term('बालः','bālaḥ'),term('बालौ','bālau'),term('बालाः','bālāḥ')],['Object',term('बालम्','bālam'),term('बालौ','bālau'),term('बालान्','bālān')]]),
 p('In the dual, the nominative and accusative coincide: bālau can be subject or object. In the plural, bālāḥ and bālān are different. Long ā occurs in both of those plural forms, so retaining vowel length matters.'),
 examples(('बालाः पठन्ति।','bālāḥ paṭhanti.','The boys read.','Plural subject with a plural verb.'),('बालिका बालान् पश्यति।','bālikā bālān paśyati.','The girl sees the boys.','Bālān is a plural object; the single girl controls singular paśyati, “sees”.'))),
 section('Transfer the pattern carefully',
 examples(('बालिका ग्रामे वसति।','bālikā grāme vasati.','The girl lives in the village.','Grāma uses the same locative pattern as bāla: grāme.'),('देवस्य नाम','devasya nāma','The god’s name.','Devasya follows the genitive pattern bālasya. Nāma means “name”; its full noun pattern is outside this lesson.')),
 p('There are sound adjustments in some words even within a broad pattern. For example, the instrumental of '+term('राम','rāma')+' is '+term('रामेण','rāmeṇa')+', with retroflex ṇ, whereas bālena has n. Do not use a substitution rule so mechanically that it erases genuine sound changes.'),
 p('Practise with grāma: choose the form for “of the village”, then “in the village”, then “from the village”. Say why you chose each case before consulting the table. Finally return to bāla and make one sentence with it as subject and one with it as object. The point is to choose forms for a purpose.'))
 ], ['The stem bāla is not the ordinary singular subject bālaḥ.', 'Bālāḥ is a plural subject; bālān is a plural object.', 'Some stems trigger sound changes: rāmeṇa has ṇ.'],
 ['Short-a masculine nouns share a useful model.', 'Learn the singular forms with their case roles.', 'Dual subject and object forms coincide; plural forms differ.'],
 [quiz('Choose “of the boy”.', ['बालम् — bālam','बालस्य — bālasya','बालाय — bālāya'],1,'Bālasya is genitive singular. Bālam is accusative; bālāya is dative.'),quiz('Which form means “the boys” as the direct object?', ['बालान् — bālān','बालाः — bālāḥ','बालः — bālaḥ'],0,'The masculine a-stem accusative plural ends in -ān.'),quiz('Choose “in the village”.', ['ग्रामस्य — grāmasya','ग्रामात् — grāmāt','ग्रामे — grāme'],2,'Grāme is locative singular; the other forms mean “of” and “from” the village.')],
 [practice('Give the singular forms “of the village”, “in the village”, and “from the village”.',term('ग्रामस्य','grāmasya','of the village')+'; '+term('ग्रामे','grāme','in the village')+'; '+term('ग्रामात्','grāmāt','from the village')+'.'),practice('Why does बालिका बालान् पश्यति। — bālikā bālān paśyati use a singular verb?','It means “The girl sees the boys”. Bālikā, the subject, is singular. Bālān is a plural direct object and does not determine the verb’s number.')], ['IV','V']),

lesson('neuter-a','Neuter nouns in a','Recognise the special subject–object pattern of phala.', ['cases'],
 ['Use phala, “fruit”, as a neuter model.', 'Recognise matching nominative and accusative forms.', 'Read neuter singular, dual, and plural forms in context.'], [
 section('A familiar stem ending, a different gender',
 p('The neuter stem '+term('फल','phala','fruit')+' ends in short a, just like masculine bāla. Its gender tells you to choose a different pattern for the nominative and accusative. The singular form is '+term('फलम्','phalam')+' whether the fruit is the subject or direct object.'),
 p('This gives you a particularly useful general rule: neuter nominative and accusative forms are identical within each number. The rule applies beyond this one stem type, although the actual endings differ among declensions. Learn both the rule and the specific forms; neither replaces the other.')),
 section('One fruit, two fruits, many fruits',
 table('Neuter phala: subject and direct object', ['Case','One','Two','Many'],[
 ['Nominative',term('फलम्','phalam'),term('फले','phale'),term('फलानि','phalāni')],['Accusative',term('फलम्','phalam'),term('फले','phale'),term('फलानि','phalāni')]]),
 p('Notice the long ā in phalāni. The dual phale is exactly two, not a vague plural. The same form phale can also be locative singular, as you will see below. Forms that coincide must be interpreted through context.'),
 examples(('फलं पतति।','phalaṃ patati.','A fruit falls.','The fruit is the subject. Patati means “falls”.'),('बालः फलं खादति।','bālaḥ phalaṃ khādati.','The boy eats a fruit.','The fruit is the object. Khādati means “eats”.'),('फलानि पतन्ति।','phalāni patanti.','Fruits fall.','Plural subject with plural patanti.')),
 p('Phalam appears as phalaṃ before a consonant in these sentences. The nasal spelling does not by itself distinguish subject from object. Ask what the verb means and which participant does the action.')),
 section('The remaining singular cases',
 table('Phala: singular forms beyond the subject and object', ['Case','Form','Typical sense'],[
 ['Instrumental',term('फलेन','phalena'),'by / with a fruit'],['Dative',term('फलाय','phalāya'),'for a fruit'],['Ablative',term('फलात्','phalāt'),'from a fruit'],['Genitive',term('फलस्य','phalasya'),'of a fruit'],['Locative',term('फले','phale'),'in / on a fruit'],['Vocative',term('फल','phala'),'O fruit!']]),
 p('These follow the same broad singular pattern as masculine a-stems outside the nominative and accusative. A vocative addressed to a fruit is unusual in everyday conversation, but the table shows the grammatical form. A full paradigm contains forms whether or not every one is equally common in daily speech.'),
 p('Compare phale in two contexts: when paired with a dual verb meaning “fall”, it can be the nominative dual, “two fruits”. In a phrase describing something inside a fruit, it can be locative singular. No single English translation belongs permanently to those letters.')),
 section('Use the model with books',
 p(term('पुस्तक','pustaka','book')+' is another neuter a-stem. Its subject and object forms are pustakam, pustake, pustakāni. Practise changing the number of books while holding the reader constant.'),
 examples(('बालिका पुस्तकं पठति।','bālikā pustakaṃ paṭhati.','The girl reads a book.','Singular object.'),('बालिका पुस्तके पठति।','bālikā pustake paṭhati.','The girl reads two books.','Here pustake is accusative dual.'),('बालिका पुस्तकानि पठति।','bālikā pustakāni paṭhati.','The girl reads books.','Plural object; the subject remains singular.')),
 p('End by covering the table and saying the three book forms. Then explain why paṭhati stays the same in all three sentences. Understanding the subject–object distinction makes the identical neuter endings much less confusing.'))
 ], ['An -am form is not always an object; it can be a neuter singular subject.', 'Phale can represent more than one case-and-number combination.', 'Preserve the long ā in phalāni and pustakāni.'],
 ['Neuter nominative and accusative match within each number.', 'Phalam, phale, phalāni are the core pattern.', 'Use the sentence to identify the role.'],
 [quiz('What are “fruits” in the nominative plural?', ['फलाः — phalāḥ','फलानि — phalāni','फले — phale'],1,'Neuter a-stems use -āni in the nominative and accusative plural.'),quiz('In फलं पतति। — phalaṃ patati (“A fruit falls”), what is phalaṃ?', ['The subject','An instrument','A direct object'],0,'The fruit is what falls; its form can be nominative despite the ending -am / -aṃ.'),quiz('Which pair of cases has matching neuter forms in every number?', ['Genitive and locative','Dative and nominative','Nominative and accusative'],2,'This is the central neuter pattern; the actual endings depend on the stem class.')],
 [practice('Change “The girl reads a book” to “The girl reads two books”.',term('बालिका पुस्तके पठति।','bālikā pustake paṭhati.','The girl reads two books.')+' Pustake is dual; paṭhati remains singular.'),practice('Why can phalam be a subject in one sentence and an object in another?','Neuter nominative and accusative are identical. The verb and the relationships in the sentence distinguish the two uses.')], ['IV','V']),

lesson('feminine-aa','Feminine nouns in ā','Follow bālikā through its most useful forms.', ['cases'],
 ['Recognise the long-ā feminine noun pattern.', 'Use bālikā in singular case roles.', 'Compare feminine subject and object forms across number.'], [
 section('Keep the final vowel long',
 p('Our feminine model is '+term('बालिका','bālikā','girl')+'. Its stem ends in long ā, and its singular nominative looks exactly like that stem. This differs from masculine bāla, whose nominative is bālaḥ. Do not add a visarga to every noun that is the subject of a sentence.'),
 p('Other regular feminine ā-stems include '+term('लता','latā','creeper')+' and '+term('माला','mālā','garland')+'. Feminine nouns also have other stem types, such as nadī, “river”. Today we learn one productive pattern, not all feminine declensions.')),
 section('The singular pattern',
 table('Bālikā: singular', ['Case','Form','Typical sense'],[
 ['Nominative',term('बालिका','bālikā'),'the girl as subject'],['Accusative',term('बालिकाम्','bālikām'),'the girl as object'],['Instrumental',term('बालिकया','bālikayā'),'by / with the girl'],['Dative',term('बालिकायै','bālikāyai'),'to / for the girl'],['Ablative',term('बालिकायाः','bālikāyāḥ'),'from the girl'],['Genitive',term('बालिकायाः','bālikāyāḥ'),'of the girl'],['Locative',term('बालिकायाम्','bālikāyām'),'in / on the girl'],['Vocative',term('बालिके','bālike'),'O girl!']]),
 p('The instrumental bālikayā has short a before yā; compare the long ā in bālikāyai and bālikāyāḥ. Read the transliteration carefully instead of treating the last several syllables as one blur. The ablative and genitive share a form, so their meaning depends on context.'),
 p('Some literal case translations are more natural with another noun. Latāyām, “on the creeper”, is an ordinary locative phrase. Bālikāyām illustrates the form, even though its use needs an appropriate context. A paradigm teaches possibilities; a sentence supplies a situation.')),
 section('Compare the three numbers',
 table('Feminine ā-stem subject and object forms', ['Role','One','Two','Many'],[
 ['Subject',term('बालिका','bālikā'),term('बालिके','bālike'),term('बालिकाः','bālikāḥ')],['Object',term('बालिकाम्','bālikām'),term('बालिके','bālike'),term('बालिकाः','bālikāḥ')]]),
 p('The dual and plural subject/object forms coincide in this pattern, while the singular distinguishes bālikā from bālikām. Bālike is also the singular vocative, “O girl!” Once again a form needs context. The reader cannot decide solely from its final letter.'),
 examples(('बालिका पठति।','bālikā paṭhati.','The girl reads.','Singular subject.'),('बालिके पठतः।','bālike paṭhataḥ.','The two girls read.','The dual verb supports reading bālike as a dual subject.'),('बालिकाः पठन्ति।','bālikāḥ paṭhanti.','The girls read.','Plural subject and plural verb.'))),
 section('Transfer the pattern and explain the choice',
 examples(('मालायाः वर्णः','mālāyāḥ varṇaḥ','The garland’s colour.','Mālāyāḥ is genitive singular. Varṇaḥ means “colour”.'),('लतायां पुष्पम्','latāyāṃ puṣpam','A flower on the creeper.','Latāyām is locative singular, written with ṃ before p. Puṣpam means “flower”.')),
 p('To build “of the garland”, first identify possession, then choose genitive singular, then use the mālā pattern to obtain mālāyāḥ. This order prevents the common mistake of choosing an ending before deciding what it needs to express.'),
 p('Practise with a sheet of paper: put bālikā, bālikām, and bālikayā in one column; write “subject”, “object”, and “by/with” in another. Match them without looking at the table. Then produce the same three forms for mālā. Finish by saying why the noun’s feminine gender does not change the present-tense verb paṭhati.'))
 ], ['Do not add ḥ to singular subject bālikā.', 'Distinguish bālikayā from bālikāyai.', 'Do not apply the ā-stem table to every feminine noun.'],
 ['The model’s stem and singular nominative are bālikā.', 'Bālikām is singular accusative; bālikayā is instrumental.', 'Several forms coincide, so read them in context.'],
 [quiz('Choose “of the girl”.', ['बालिकया — bālikayā','बालिकाम् — bālikām','बालिकायाः — bālikāyāḥ'],2,'Bālikāyāḥ is genitive singular; it can also be ablative in another context.'),quiz('Which is the singular subject form?', ['बालिका — bālikā','बालिकाः — bālikāḥ','बालिकाम् — bālikām'],0,'Bālikā is nominative singular. The visarga form bālikāḥ is plural here.'),quiz('How do you say “by / with the garland”?', ['मालायै — mālāyai','मालया — mālayā','मालाम् — mālām'],1,'Mālayā follows the instrumental pattern bālikayā.')],
 [practice('Give the object forms for one, two, and many girls.',term('बालिकाम् बालिके बालिकाः','bālikām bālike bālikāḥ')+'. These are accusative singular, dual, and plural.'),practice('Give “of the creeper” and “on the creeper”.',term('लतायाः','latāyāḥ','of the creeper')+'; '+term('लतायाम्','latāyām','on the creeper')+'. Choose genitive for possession and locative for location.')], ['IV','V']),

lesson('pronouns','I, you, he, she & it','Replace repeated nouns while keeping person and number clear.', ['gender','number','cases'],
 ['Use basic subject pronouns in three numbers.', 'Distinguish the speaker, listener, and person spoken about.', 'Recognise common possessive forms without inventing noun-like endings.'], [
 section('A pronoun points to someone or something',
 p('A pronoun lets us refer to a participant without repeating a name. “I” is the speaker, “you” is the listener, and “he”, “she”, or “it” refers to someone or something spoken about. These grammatical persons help determine the verb form. Do not confuse person with gender: a first-person speaker can have any gender.'),
 p('English and traditional Sanskrit grammar use different numbering conventions for person names. This course labels them by meaning—speaker, listener, and person spoken about—alongside English first, second, and third person. That keeps the choices clear while you are beginning.')),
 section('Speaker and listener: subject forms',
 table('Nominative pronouns', ['Person','One','Two','Many'],[
 ['Speaker: first person',term('अहम्','aham','I'),term('आवाम्','āvām','we two'),term('वयम्','vayam','we')],['Listener: second person',term('त्वम्','tvam','you'),term('युवाम्','yuvām','you two'),term('यूयम्','yūyam','you all')]]),
 p('These pronouns do not distinguish masculine, feminine, and neuter. Aham can be spoken by anyone. Their forms are irregular, so do not attach the ordinary bāla or bālikā endings to them. Learn the forms you need as a small family.'),
 p('Before a consonant, a final m is often written as anusvāra: aham becomes ahaṃ in ahaṃ paṭhāmi. That spelling change is not a new person or number. The transliteration reflects the Devanagari exactly.')),
 section('The person or thing spoken about',
 table('Common nominative forms of tad, “that”', ['Gender','One','Two','Many'],[
 ['Masculine',term('सः','saḥ','he / that'),term('तौ','tau','those two'),term('ते','te','they / those')],['Feminine',term('सा','sā','she / that'),term('ते','te','those two'),term('ताः','tāḥ','they / those')],['Neuter',term('तत्','tat','it / that'),term('ते','te','those two'),term('तानि','tāni','they / those')]]),
 p('These are demonstrative forms that often serve where English uses he, she, and it. Notice that te has several possible gender-and-number readings. Context matters, just as it did with noun forms. The gender agrees with the noun referred to; it is not always inferred from the English word “it”.'),
 examples(('सः पठति।','saḥ paṭhati.','He reads.','Masculine singular subject pronoun.'),('सा पठति।','sā paṭhati.','She reads.','Feminine singular subject pronoun; the verb is unchanged.'),('ते पठन्ति।','te paṭhanti.','They read.','Here te is masculine plural, supported by the plural verb.'))),
 section('A few useful possessive forms',
 p('Pronouns change case too. For “my” or “of me”, use '+term('मम','mama')+'; for “your” or “of you” singular, use '+term('तव','tava')+'. These are genitives. Do not create forms by adding -sya to aham or tvam.'),
 examples(('मम पुस्तकम्','mama pustakam','My book.','Mama marks the possessor.'),('तव माला','tava mālā','Your garland.','Tava is used regardless of the grammatical gender of the possessed noun.'),('अहं पठामि।','ahaṃ paṭhāmi.','I read.','The speaker pronoun takes a first-person verb.'),('त्वं पठसि।','tvaṃ paṭhasi.','You read.','The listener pronoun takes a second-person singular verb.')),
 p('Sanskrit can omit a subject pronoun when the verb ending and context make the subject clear. Paṭhāmi alone can mean “I read”. We retain pronouns in many beginner examples to make agreement visible. Practise replacing a repeated noun with a suitable pronoun, then check both number and verb form.'))
 ], ['Aham and tvam do not change for the speaker’s or listener’s gender.', 'Do not invent ahamasya for “my”: the form is mama.', 'Te is ambiguous in isolation; inspect its context.'],
 ['Person distinguishes speaker, listener, and someone spoken about.', 'Subject pronouns have singular, dual, and plural forms.', 'Mama and tava are useful genitives.'],
 [quiz('Which pronoun means “we two”?', ['वयम् — vayam','आवाम् — āvām','युवाम् — yuvām'],1,'Āvām is first-person dual. Vayam is plural; yuvām means “you two”.'),quiz('Choose “my book”.', ['मम पुस्तकम् — mama pustakam','तव पुस्तकम् — tava pustakam','त्वं पुस्तकम् — tvaṃ pustakam'],0,'Mama is the genitive meaning “of me” or “my”.'),quiz('Which statement about अहम् — aham is correct?', ['It is only masculine','It always means two speakers','It does not distinguish gender'],2,'First- and second-person pronouns have no gender distinction.')],
 [practice('Replace बालिका bālikā with “she” in बालिका पठति। — bālikā paṭhati.',term('सा पठति।','sā paṭhati.','She reads.')+' The verb remains third-person singular.'),practice('Distinguish आवाम् āvām, युवाम् yuvām, and वयम् vayam.', 'Āvām: we two. Yuvām: you two. Vayam: we, more than two. The first two are dual; the last is plural.')], ['VII']),

lesson('present-verbs','Present-tense verbs','Match a verb to who acts and how many act.', ['number','pronouns'],
 ['Use the nine present-tense forms of paṭh.', 'Distinguish a verbal root from a present stem.', 'Match person and number without changing a verb for gender.'], [
 section('The ending supplies more than time',
 p('A finite verb can tell us the action, time or mood, person, and number. Our focus is the active present tense, often called laṭ in traditional instruction. '+term('पठति','paṭhati')+' can mean “reads” or “is reading”; the context decides which English translation is more natural.'),
 p('A verbal root is a base of meaning, conventionally written with a root sign: √paṭh, “read or recite”. The present stem in this model is paṭha-. Person-and-number endings combine with that stem. Some vowels change in the process, so learn the resulting forms rather than simply joining written pieces mechanically.')),
 section('One model, nine forms',
 table('Paṭh: active present indicative', ['Who?','One','Two','Many'],[
 ['Spoken about: third person',term('पठति','paṭhati'),term('पठतः','paṭhataḥ'),term('पठन्ति','paṭhanti')],['Listener: second person',term('पठसि','paṭhasi'),term('पठथः','paṭhathaḥ'),term('पठथ','paṭhatha')],['Speaker: first person',term('पठामि','paṭhāmi'),term('पठावः','paṭhāvaḥ'),term('पठामः','paṭhāmaḥ')]]),
 p('Begin with the three singular forms: paṭhati, paṭhasi, paṭhāmi. Then add the dual and plural. The first-person row has long ā. Notice especially paṭhataḥ, “they two read”, versus paṭhathaḥ, “you two read”: t and th are different consonants.'),
 p('Traditional Sanskrit labels prathama, madhyama, and uttama correspond here to someone spoken about, the listener, and the speaker respectively. In English grammatical terminology these are third, second, and first person. Use the meaning of the row as your guide.')),
 section('Attach a subject and check the match',
 examples(('अहं पठामि।','ahaṃ paṭhāmi.','I read.','First-person singular.'),('त्वं पठसि।','tvaṃ paṭhasi.','You read.','Second-person singular.'),('आवां पठावः।','āvāṃ paṭhāvaḥ.','We two read.','First-person dual.'),('यूयं पठथ।','yūyaṃ paṭhatha.','You all read.','Second-person plural.'),('बालिकाः पठन्ति।','bālikāḥ paṭhanti.','The girls read.','Third-person plural.')),
 p('A named person or ordinary noun subject uses third-person forms. Bālikā is grammatically third person even when that person is standing nearby. The form changes to second person when you directly address the listener as “you”. The distinction is about speech roles, not physical distance.'),
 p('In these present forms, gender does not change the verb. Saḥ paṭhati and sā paṭhati use the same verb. The object’s number also does not control the verb: one reader of many books still takes a singular form.')),
 section('Extend the pattern, but not to every root',
 p('You can practise a similar present pattern with '+term('लिखति','likhati','writes')+' and '+term('क्रीडति','krīḍati','plays')+'. For example, likhāmi means “I write”, and krīḍanti means “they play”. First identify the present stem given in your vocabulary; some roots change considerably before the endings are added.'),
 p('Not every Sanskrit verb is made by attaching -ati to a root. Sanskrit has several present-stem classes and another set of endings called middle endings. Neither those full systems nor other tenses are required for this foundation course. Learn a small number of reliable present forms and use them accurately.'),
 p('For a two-minute drill, select a pronoun from the previous lesson and give the matching form of paṭh. Then replace the pronoun with a noun where possible. Finally add pustakam as an object. Check person, number, and meaning before reading the sentence aloud.'))
 ], ['Paṭhataḥ (“they two”) and paṭhathaḥ (“you two”) differ.', 'Do not use paṭhati for every person.', 'Do not generalise this present-stem model to every Sanskrit root.'],
 ['Choose person and number before choosing a verb form.', 'Paṭhati, paṭhasi, paṭhāmi are the singular core.', 'Subject agreement is independent of object number.'],
 [quiz('Complete अहं … — ahaṃ … (“I read”).', ['पठति — paṭhati','पठसि — paṭhasi','पठामि — paṭhāmi'],2,'Aham is first-person singular, so choose paṭhāmi.'),quiz('Choose “you two read”.', ['पठतः — paṭhataḥ','पठथः — paṭhathaḥ','पठथ — paṭhatha'],1,'Paṭhathaḥ is second-person dual. The aspirated th distinguishes it from third-person dual paṭhataḥ.'),quiz('Which form fits वयम् — vayam (“we”)?', ['पठामः — paṭhāmaḥ','पठन्ति — paṭhanti','पठावः — paṭhāvaḥ'],0,'Vayam takes first-person plural paṭhāmaḥ.')],
 [practice('Write “We two read a book”.',term('आवां पुस्तकं पठावः।','āvāṃ pustakaṃ paṭhāvaḥ.','We two read a book.')+' The dual speaker pronoun matches first-person dual paṭhāvaḥ.'),practice('Correct त्वं पठति। — tvaṃ paṭhati.',term('त्वं पठसि।','tvaṃ paṭhasi.','You read.')+' Tvam is second-person singular, so use paṭhasi.')], ['IX']),

lesson('build-sentences','Build your own sentences','Bring roles, noun forms, and verb agreement together.', ['masculine-a','neuter-a','feminine-aa','pronouns','present-verbs'],
 ['Plan a sentence from its meaning.', 'Choose case and number for each noun.', 'Check agreement and explain your choices.'], [
 section('Start with a thought you can explain',
 p('You now have enough grammar to create small, complete sentences. Begin with a clear meaning, such as “The girl reads a book”. Resist translating an English sentence word by word from left to right. Instead, identify the action and its participants, then choose each Sanskrit form for its job.'),
 p('Use this sequence: choose the verb’s meaning; identify the subject; identify any direct object; choose number and case for the nouns; choose person and number for the verb. Add possession or location only after that core is working. Finally read the whole sentence and translate it back into English.'),
 note('These exercises continue to keep word boundaries and grammatical forms visible. Full external sandhi is outside this course. Some combinations therefore appear in a deliberately separated teaching form rather than as continuous classical prose.')),
 section('Work through one sentence',
 table('Plan: “The two girls read books”', ['Decision','Reason','Chosen form'],[
 ['Subject','Girls: feminine, exactly two, nominative',term('बालिके','bālike')],['Object','Books: neuter, plural, accusative',term('पुस्तकानि','pustakāni')],['Verb','Read: third person, dual, present',term('पठतः','paṭhataḥ')]]),
 examples(('बालिके पुस्तकानि पठतः।','bālike pustakāni paṭhataḥ.','The two girls read books.','The dual subject controls the dual verb; the plural object has its own number.')),
 p('The noun bālike looks the same in nominative and accusative dual, but here it is the subject because the girls are reading. Pustakāni is the direct object. This is why understanding the meaning and verb is essential even when you recognise all the endings.'),
 p('Change only the subject to one girl: bālikā pustakāni paṭhati. Both the noun and verb change to singular; the object stays plural. Change only the object to one book: bālike pustakaṃ paṭhataḥ. Now the dual subject and verb remain unchanged.')),
 section('Add possession or location',
 examples(('बालिका मम पुस्तकं पठति।','bālikā mama pustakaṃ paṭhati.','The girl reads my book.','Mama, “my”, identifies the possessor of the book.'),('बालिका ग्रामे पुस्तकं पठति।','bālikā grāme pustakaṃ paṭhati.','The girl reads a book in the village.','Grāme is locative singular; it gives the location.'),('अहं पुस्तकं लिखामि।','ahaṃ pustakaṃ likhāmi.','I write a book.','Aham requires the first-person singular likhāmi.')),
 p('Each addition has its own job. The genitive possessor does not become the subject merely because it names a person. The locative does not become the direct object merely because it occurs before the verb. If a longer sentence becomes confusing, temporarily remove the extra information and find the core subject and verb again.'),
 p('A noun and its adjective agree with each other, while the subject and the finite verb agree in person and number. These are related checks but not identical ones. In sundarā bālikā paṭhati, sundarā matches the feminine singular subject; paṭhati remains third-person singular.')),
 section('Learn from a deliberate mistake',
 p('Consider '+term('बालौ पठति।','bālau paṭhati.')+'. The noun means “two boys” as subject, but the verb means “he/she/it reads”. The number labels disagree. Repair the verb to produce '+term('बालौ पठतः।','bālau paṭhataḥ.','The two boys read.')+'. A useful correction explains the reason rather than replacing a word by guesswork.'),
 p('Another common error is to use a masculine plural subject ending with a neuter noun. Books are pustakāni in the nominative and accusative plural, not pustakāḥ. When uncertain, return to the noun’s stem and gender, then pick the correct model.'),
 p('Word order can vary in Sanskrit. Our subject–object–verb order is a practice aid rather than a rule that every text must follow. As your reading grows, rely more on case endings, agreement, the verb’s meaning, and context.')),
 section('Your first independent paragraph',
 p('Write three connected thoughts: “I read a book. The girl writes. The two boys play.” Choose each form before looking at the solution in the practice section. Then swap one subject or object and explain every ending that must change.'),
 p('This foundation is a beginning. You can now approach a simple sentence by identifying its action, participants, and relationships. When you meet an unfamiliar stem or tense, consult a reference rather than forcing it into the patterns here. Revisit any branch where choosing forms still feels uncertain; completing the tree never locks a lesson away.'))
 ], ['Check the subject’s number, not the nearest noun’s number.', 'Use the correct gender-and-stem pattern for each noun.', 'Do not treat our teaching word order as mandatory in all Sanskrit.'],
 ['Meaning → roles → noun forms → verb agreement.', 'Add possession and location after the core sentence works.', 'Explain a correction by naming the mismatch.'],
 [quiz('Choose “The two girls read books”.', ['बालिके पुस्तकानि पठतः। — bālike pustakāni paṭhataḥ.','बालिके पुस्तकानि पठति। — bālike pustakāni paṭhati.','बालिका पुस्तकानि पठतः। — bālikā pustakāni paṭhataḥ.'],0,'Both bālike and paṭhataḥ are dual; pustakāni is the plural object.'),quiz('What must change when अहं पठामि (“I read”) becomes “You read”?', ['Only the noun’s gender','The subject pronoun and the verb’s person','Only the spelling of the vowel'],1,'Use tvaṃ paṭhasi: second-person singular pronoun and verb.'),quiz('Which form adds “in the village”?', ['ग्रामस्य — grāmasya','ग्रामम् — grāmam','ग्रामे — grāme'],2,'Grāme is locative singular and supplies the location.')],
 [practice('Translate: “I read a book. The girl writes. The two boys play.”',term('अहं पुस्तकं पठामि।','ahaṃ pustakaṃ paṭhāmi.','I read a book.')+'<br>'+term('बालिका लिखति।','bālikā likhati.','The girl writes.')+'<br>'+term('बालौ क्रीडतः।','bālau krīḍataḥ.','The two boys play.')+' The verbs are first-person singular, third-person singular, and third-person dual.'),practice('Write “The girls read my book in the village”.',term('बालिकाः ग्रामे मम पुस्तकं पठन्ति।','bālikāḥ grāme mama pustakaṃ paṭhanti.','The girls read my book in the village.')+' Bālikāḥ is nominative plural, grāme locative singular, mama genitive, pustakaṃ accusative singular, and paṭhanti third-person plural.'),practice('Correct बालौ पठति। — bālau paṭhati and explain the problem.',term('बालौ पठतः।','bālau paṭhataḥ.','The two boys read.')+' The dual subject needs a dual verb, not singular paṭhati.')], ['IV','V','VII','IX']),
]

STAGES = [
 ('Find your footing', ['sounds']),
 ('Connect sound to script', ['script']),
 ('Meet the sentence', ['sentence-parts']),
 ('Explore two features of a noun', ['gender', 'number']),
 ('Understand each word’s job', ['cases']),
 ('Follow the three noun branches', ['masculine-a', 'neuter-a', 'feminine-aa']),
 ('Bring people and actions together', ['pronouns', 'present-verbs']),
 ('Put it all together', ['build-sentences']),
]
