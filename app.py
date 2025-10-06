import streamlit as st

# Page config
st.set_page_config(page_title="PHL 201 Comprehensive Exam Quiz", page_icon="🧠", layout="wide")

# Initialize session state
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# Questions data - All 120 questions from PHL 201 Exam
questions = [
    # SECTION 1: EPISTEMOLOGY (1-30)
    {
        "id": 1,
        "question": "What is epistemology?",
        "options": [
            "The study of being and existence",
            "The study of knowledge and truth",
            "The study of ethics and morality",
            "The study of logic and argumentation"
        ],
        "correct": 1,
        "section": "Epistemology"
    },
    {
        "id": 2,
        "question": "The classical definition of knowledge is:",
        "options": [
            "True belief",
            "Justified true belief",
            "Certain belief",
            "Popular belief"
        ],
        "correct": 1,
        "section": "Epistemology"
    },
    {
        "id": 3,
        "question": "The Gettier problem challenges:",
        "options": [
            "The existence of truth",
            "The classical definition of knowledge as justified true belief",
            "The possibility of belief",
            "The need for justification"
        ],
        "correct": 1,
        "section": "Epistemology"
    },
    {
        "id": 4,
        "question": "Rationalism emphasizes:",
        "options": [
            "Experience only",
            "Reason and logic",
            "Authority",
            "Intuition only"
        ],
        "correct": 1,
        "section": "Epistemology"
    },
    {
        "id": 5,
        "question": "Empiricism emphasizes:",
        "options": [
            "Reason only",
            "Sensory experience and observation",
            "Revelation",
            "Mathematical proof"
        ],
        "correct": 1,
        "section": "Epistemology"
    },
    {
        "id": 6,
        "question": "A priori knowledge:",
        "options": [
            "Requires experience",
            "Can be known independently of experience",
            "Comes from authorities",
            "Changes over time"
        ],
        "correct": 1,
        "section": "Epistemology"
    },
    {
        "id": 7,
        "question": "A posteriori knowledge requires:",
        "options": [
            "Pure reasoning only",
            "Experience and observation",
            "Mathematical proof",
            "Authority confirmation"
        ],
        "correct": 1,
        "section": "Epistemology"
    },
    {
        "id": 8,
        "question": "Skepticism questions:",
        "options": [
            "Religious beliefs only",
            "Whether knowledge is possible",
            "Scientific claims only",
            "Arguments only"
        ],
        "correct": 1,
        "section": "Epistemology"
    },
    {
        "id": 9,
        "question": "Foundationalism claims:",
        "options": [
            "All beliefs are equal",
            "Some beliefs are basic and need no justification from others",
            "No beliefs can be justified",
            "Only empirical beliefs count"
        ],
        "correct": 1,
        "section": "Epistemology"
    },
    {
        "id": 10,
        "question": "Coherentism argues:",
        "options": [
            "Only foundations matter",
            "Beliefs are justified by fitting coherently together",
            "No justification is possible",
            "Only experience matters"
        ],
        "correct": 1,
        "section": "Epistemology"
    },
    {
        "id": 11,
        "question": "Reliabilism judges knowledge based on:",
        "options": [
            "Popular consensus",
            "Whether the belief-forming process is reliable",
            "Authority endorsement",
            "Emotional certainty"
        ],
        "correct": 1,
        "section": "Epistemology"
    },
    {
        "id": 12,
        "question": "Knowledge differs from opinion because:",
        "options": [
            "Knowledge is popular",
            "Knowledge has rational justification and corresponds to reality",
            "Knowledge is easier",
            "Knowledge never changes"
        ],
        "correct": 1,
        "section": "Epistemology"
    },
    {
        "id": 13,
        "question": "Internalism in epistemology holds that:",
        "options": [
            "Knowledge comes from within",
            "The factors that justify belief must be accessible to the believer",
            "Only internal states exist",
            "The external world is irrelevant"
        ],
        "correct": 1,
        "section": "Epistemology"
    },
    {
        "id": 14,
        "question": "Externalism in epistemology argues:",
        "options": [
            "Only external things exist",
            "Justification can depend on factors outside the believer's awareness",
            "Knowledge is impossible",
            "Only empirical knowledge counts"
        ],
        "correct": 1,
        "section": "Epistemology"
    },
    {
        "id": 15,
        "question": "The correspondence theory of truth states:",
        "options": [
            "Truth is what most believe",
            "Truth consists in agreement of thoughts with reality",
            "Truth is whatever works",
            "Truth doesn't exist"
        ],
        "correct": 1,
        "section": "Epistemology"
    },
    {
        "id": 16,
        "question": "The tripartite definition of knowledge requires:",
        "options": [
            "Only truth",
            "Belief, truth, and justification",
            "Only justification",
            "Only belief"
        ],
        "correct": 1,
        "section": "Epistemology"
    },
    {
        "id": 17,
        "question": "Fallibilism holds that:",
        "options": [
            "We can never be wrong",
            "Knowledge doesn't require absolute certainty",
            "All beliefs are false",
            "Only certain beliefs count as knowledge"
        ],
        "correct": 1,
        "section": "Epistemology"
    },
    {
        "id": 18,
        "question": "The regress problem in epistemology concerns:",
        "options": [
            "Going backwards in time",
            "The infinite chain of justification for beliefs",
            "Forgetting information",
            "Repeating mistakes"
        ],
        "correct": 1,
        "section": "Epistemology"
    },
    {
        "id": 19,
        "question": "Virtue epistemology focuses on:",
        "options": [
            "Moral virtues only",
            "Intellectual virtues and excellences in knowing",
            "Social virtues",
            "Physical abilities"
        ],
        "correct": 1,
        "section": "Epistemology"
    },
    {
        "id": 20,
        "question": "Contextualism in epistemology claims:",
        "options": [
            "Context never matters",
            "Knowledge attributions are context-sensitive",
            "Only context matters",
            "Context is irrelevant to truth"
        ],
        "correct": 1,
        "section": "Epistemology"
    },
    {
        "id": 21,
        "question": "The value problem asks:",
        "options": [
            "How much knowledge costs",
            "Why knowledge is more valuable than mere true belief",
            "Which knowledge is most important",
            "How to measure knowledge"
        ],
        "correct": 1,
        "section": "Epistemology"
    },
    {
        "id": 22,
        "question": "What distinguishes knowledge from lucky guesses?",
        "options": [
            "Knowledge is always certain",
            "Knowledge has proper justification and isn't accidental",
            "Knowledge is more popular",
            "Knowledge is simpler"
        ],
        "correct": 1,
        "section": "Epistemology"
    },
    {
        "id": 23,
        "question": "According to course readings, precise definition matters because:",
        "options": [
            "It sounds academic",
            "Imprecise claims cannot be properly evaluated",
            "It makes arguments longer",
            "It confuses opponents"
        ],
        "correct": 1,
        "section": "Epistemology"
    },
    {
        "id": 24,
        "question": "Epistemic circularity occurs when:",
        "options": [
            "Using circular reasoning",
            "Using a source of knowledge to validate itself",
            "Avoiding all reasoning",
            "Only trusting authorities"
        ],
        "correct": 1,
        "section": "Epistemology"
    },
    {
        "id": 25,
        "question": "The problem of the criterion refers to:",
        "options": [
            "Measuring difficulty",
            "The circular challenge of needing criteria for truth to establish criteria",
            "Education cost",
            "Learning time"
        ],
        "correct": 1,
        "section": "Epistemology"
    },
    {
        "id": 26,
        "question": "Modal epistemology deals with:",
        "options": [
            "Only necessary truths",
            "Knowledge of possibility and necessity",
            "Only empirical facts",
            "Only logical truths"
        ],
        "correct": 1,
        "section": "Epistemology"
    },
    {
        "id": 27,
        "question": "What is a philosophical claim?",
        "options": [
            "An emotion",
            "A declarative sentence that can be true or false",
            "A question",
            "A belief without justification"
        ],
        "correct": 1,
        "section": "Epistemology"
    },
    {
        "id": 28,
        "question": "A vague claim:",
        "options": [
            "Is about abstracts",
            "Uses imprecise words with unclear boundaries",
            "Is controversial",
            "Is complex"
        ],
        "correct": 1,
        "section": "Epistemology"
    },
    {
        "id": 29,
        "question": "An ambiguous claim:",
        "options": [
            "Is false",
            "Can have several possible meanings",
            "Is simple",
            "Needs expertise"
        ],
        "correct": 1,
        "section": "Epistemology"
    },
    {
        "id": 30,
        "question": "To avoid vagueness:",
        "options": [
            "Use technical terms",
            "Define terms through examples, synonyms, or explanations",
            "Avoid topics",
            "Discuss facts only"
        ],
        "correct": 1,
        "section": "Epistemology"
    },
    
    # SECTION 2: PLATO'S THEORY OF FORMS (31-50)
    {
        "id": 31,
        "question": "According to Plato, the world we perceive through our senses is:",
        "options": [
            "The most real and reliable source of knowledge",
            "An imperfect copy of a more perfect reality",
            "An illusion that doesn't exist at all",
            "The only world that exists"
        ],
        "correct": 1,
        "section": "Plato's Theory of Forms"
    },
    {
        "id": 32,
        "question": "In Plato's Theory of Forms, what makes the Forms 'more real' than material objects?",
        "options": [
            "Forms are bigger and more powerful than physical things",
            "Forms are eternal, unchanging, and perfect while material things are temporary and flawed",
            "Forms can be seen with our eyes while material things are invisible",
            "Forms are located in a specific place while material things exist everywhere"
        ],
        "correct": 1,
        "section": "Plato's Theory of Forms"
    },
    {
        "id": 33,
        "question": "What does the 'participation' relationship mean in Plato's theory?",
        "options": [
            "Forms actively participate in creating the material world",
            "Material objects are imperfect copies that 'participate in' or resemble perfect Forms",
            "Humans participate in Forms through religious ceremonies",
            "Forms and material objects are equal participants in reality"
        ],
        "correct": 1,
        "section": "Plato's Theory of Forms"
    },
    {
        "id": 34,
        "question": "According to Plato, why can we recognize that a drawn triangle is triangular even though it's imperfect?",
        "options": [
            "Because we learned geometry in school",
            "Because our soul has knowledge of the perfect Form of Triangle from before birth",
            "Because all triangles in the physical world are actually perfect",
            "Because recognition is just a learned behavioral response"
        ],
        "correct": 1,
        "section": "Plato's Theory of Forms"
    },
    {
        "id": 35,
        "question": "What is the Form of the Good in Plato's theory?",
        "options": [
            "Just another Form like all the others",
            "The highest Form that makes all other Forms knowable and gives them reality",
            "A form that only exists in human minds",
            "The least important of all Forms"
        ],
        "correct": 1,
        "section": "Plato's Theory of Forms"
    },
    {
        "id": 36,
        "question": "In Plato's Divided Line analogy, which represents the highest level of knowledge?",
        "options": [
            "Images and shadows (eikasia)",
            "Physical objects (pistis)",
            "Mathematical reasoning (dianoia)",
            "Knowledge of Forms through dialectic (noesis)"
        ],
        "correct": 3,
        "section": "Plato's Theory of Forms"
    },
    {
        "id": 37,
        "question": "Which of these would Plato consider closest to true reality?",
        "options": [
            "A photograph of a beautiful sunset",
            "The actual sunset in the physical world",
            "The mathematical equations describing light and color",
            "The Form of Beauty itself"
        ],
        "correct": 3,
        "section": "Plato's Theory of Forms"
    },
    {
        "id": 38,
        "question": "What does Plato mean when he says philosophers should rule?",
        "options": [
            "Philosophers are naturally more ambitious than others",
            "Only philosophers have seen true reality and can guide others toward it",
            "Philosophers are better at making money than others",
            "Philosophy is the easiest subject to master"
        ],
        "correct": 1,
        "section": "Plato's Theory of Forms"
    },
    {
        "id": 39,
        "question": "How does Plato's theory explain why we can understand abstract mathematical concepts?",
        "options": [
            "Mathematics is learned through sensory experience",
            "The soul has prior knowledge of perfect mathematical Forms",
            "Mathematical concepts are just useful human conventions",
            "Mathematics doesn't really exist, it's just language"
        ],
        "correct": 1,
        "section": "Plato's Theory of Forms"
    },
    {
        "id": 40,
        "question": "According to Plato, what is the relationship between justice in the soul and justice in the state?",
        "options": [
            "There is no relationship between individual and political justice",
            "Both involve the same structure: reason ruling over spirit and appetite",
            "Political justice is more important than individual justice",
            "Individual justice is impossible without political justice"
        ],
        "correct": 1,
        "section": "Plato's Theory of Forms"
    },
    {
        "id": 41,
        "question": "In the Cave Allegory, what do the shadows on the wall represent?",
        "options": [
            "Evil or false ideas that deceive people",
            "Sensory experiences that we mistake for ultimate reality",
            "Mathematical concepts that are hard to understand",
            "Political propaganda used to control people"
        ],
        "correct": 1,
        "section": "Plato's Theory of Forms"
    },
    {
        "id": 42,
        "question": "What does the journey from cave to sunlight represent?",
        "options": [
            "Growing up and becoming an adult",
            "The process of philosophical education and enlightenment",
            "Escaping from political oppression",
            "Learning to use your physical senses better"
        ],
        "correct": 1,
        "section": "Plato's Theory of Forms"
    },
    {
        "id": 43,
        "question": "Why does the escaped prisoner return to the cave?",
        "options": [
            "He realizes the outside world was just another illusion",
            "He wants to rule over the other prisoners",
            "He feels a duty to help others reach enlightenment",
            "He is forced to return against his will"
        ],
        "correct": 2,
        "section": "Plato's Theory of Forms"
    },
    {
        "id": 44,
        "question": "According to Plato, why do people resist philosophical truth?",
        "options": [
            "Because they are naturally evil or stupid",
            "Because truth is painful and they prefer comfortable illusions",
            "Because philosophers explain things poorly",
            "Because there is no real truth to discover"
        ],
        "correct": 1,
        "section": "Plato's Theory of Forms"
    },
    {
        "id": 45,
        "question": "What does the sun represent in the Cave Allegory?",
        "options": [
            "Physical warmth and comfort",
            "The Form of the Good - the highest source of knowledge and reality",
            "Human emotions and feelings",
            "Political power and authority"
        ],
        "correct": 1,
        "section": "Plato's Theory of Forms"
    },
    {
        "id": 46,
        "question": "What does Plato suggest about the relationship between knowledge and moral responsibility?",
        "options": [
            "Knowledge has nothing to do with moral responsibility",
            "Those who have achieved knowledge have a duty to help others",
            "Knowledge makes people selfish and uncaring",
            "Only some people deserve to have knowledge"
        ],
        "correct": 1,
        "section": "Plato's Theory of Forms"
    },
    {
        "id": 47,
        "question": "How does Plato's theory explain moral knowledge?",
        "options": [
            "Moral knowledge comes from cultural conditioning",
            "Moral knowledge comes from recognizing eternal moral Forms like Justice and Good",
            "There is no such thing as moral knowledge",
            "Moral knowledge is purely emotional"
        ],
        "correct": 1,
        "section": "Plato's Theory of Forms"
    },
    {
        "id": 48,
        "question": "According to Plato, why is the physical world less real than the Forms?",
        "options": [
            "The physical world doesn't exist at all",
            "The physical world is constantly changing and imperfect, while Forms are eternal and perfect",
            "The physical world is too small compared to the Forms",
            "The physical world is evil while Forms are good"
        ],
        "correct": 1,
        "section": "Plato's Theory of Forms"
    },
    {
        "id": 49,
        "question": "How does Plato's theory explain why mathematical truths are universal?",
        "options": [
            "Different cultures create different mathematics",
            "Mathematical Forms exist eternally and can be discovered by any rational mind",
            "Mathematics is just a useful convention",
            "Mathematical truths are not actually universal"
        ],
        "correct": 1,
        "section": "Plato's Theory of Forms"
    },
    {
        "id": 50,
        "question": "What is Aristotle's 'Third Man' argument against Plato's Forms?",
        "options": [
            "There must be three versions of every Form",
            "If humans resemble the Form of Human, we need another Form to explain that resemblance, leading to infinite regress",
            "Only three people can understand each Form",
            "Forms exist in groups of three"
        ],
        "correct": 1,
        "section": "Plato's Theory of Forms"
    },
    
    # SECTION 3: SOCRATES AND ANCIENT PHILOSOPHY (51-70)
    {
        "id": 51,
        "question": "Why was Socrates put on trial?",
        "options": [
            "For stealing money from the state",
            "For corrupting the youth of Athens and not believing in the gods of the state",
            "For supporting Athens' enemies in war",
            "For teaching without a license"
        ],
        "correct": 1,
        "section": "Socrates and Ancient Philosophy"
    },
    {
        "id": 52,
        "question": "What was Socrates' response to the Oracle at Delphi saying he was the wisest person?",
        "options": [
            "He immediately accepted this as proof of his superiority",
            "He tested this by questioning people who claimed to have knowledge",
            "He rejected the Oracle as false",
            "He stopped doing philosophy altogether"
        ],
        "correct": 1,
        "section": "Socrates and Ancient Philosophy"
    },
    {
        "id": 53,
        "question": "Socrates' method of questioning is designed to:",
        "options": [
            "Prove that he is smarter than everyone else",
            "Show people that they don't really know what they think they know",
            "Teach specific facts about the world",
            "Win debates against opponents"
        ],
        "correct": 1,
        "section": "Socrates and Ancient Philosophy"
    },
    {
        "id": 54,
        "question": "According to Socrates in the Crito, why shouldn't he escape from prison?",
        "options": [
            "Because escape is physically impossible",
            "Because he has an obligation to obey the laws that gave him life and education",
            "Because he wants to become a martyr",
            "Because his friends refuse to help him"
        ],
        "correct": 1,
        "section": "Socrates and Ancient Philosophy"
    },
    {
        "id": 55,
        "question": "In his trial defense, Socrates compares himself to:",
        "options": [
            "A wise teacher",
            "A gadfly that stings the state into action",
            "A military general",
            "A religious prophet"
        ],
        "correct": 1,
        "section": "Socrates and Ancient Philosophy"
    },
    {
        "id": 56,
        "question": "What does Socrates mean when he says 'the unexamined life is not worth living'?",
        "options": [
            "Life without scientific study is meaningless",
            "A life without philosophical self-reflection lacks value",
            "Only philosophers should be allowed to live",
            "People should constantly worry about their lives"
        ],
        "correct": 1,
        "section": "Socrates and Ancient Philosophy"
    },
    {
        "id": 57,
        "question": "What is the significance of Socrates' claim that he knows nothing?",
        "options": [
            "It shows he is being falsely modest",
            "It demonstrates intellectual humility and the beginning of true wisdom",
            "It proves that knowledge is impossible",
            "It means he never studied anything"
        ],
        "correct": 1,
        "section": "Socrates and Ancient Philosophy"
    },
    {
        "id": 58,
        "question": "In Socrates' view, what is the relationship between knowledge and virtue?",
        "options": [
            "Knowledge and virtue are completely unrelated",
            "True knowledge leads to virtuous action - no one does wrong willingly",
            "Virtue is more important than knowledge",
            "Knowledge corrupts virtue"
        ],
        "correct": 1,
        "section": "Socrates and Ancient Philosophy"
    },
    {
        "id": 59,
        "question": "What does philosophy literally mean?",
        "options": [
            "The study of wisdom",
            "The love of wisdom",
            "The pursuit of truth",
            "The analysis of reality"
        ],
        "correct": 1,
        "section": "Socrates and Ancient Philosophy"
    },
    {
        "id": 60,
        "question": "According to the text, what is the primary goal of philosophy?",
        "options": [
            "To win arguments against others",
            "To achieve autonomy by examining fundamental beliefs and encouraging rational thinking",
            "To memorize the thoughts of ancient thinkers",
            "To prove that all knowledge is relative"
        ],
        "correct": 1,
        "section": "Socrates and Ancient Philosophy"
    },
    {
        "id": 61,
        "question": "What are the three main traditional fields of philosophy?",
        "options": [
            "Logic, ethics, and politics",
            "Epistemology, metaphysics, and ethics",
            "Theology, science, and morality",
            "Ancient, medieval, and modern"
        ],
        "correct": 1,
        "section": "Socrates and Ancient Philosophy"
    },
    {
        "id": 62,
        "question": "Critical thinking involves:",
        "options": [
            "Always disagreeing with popular opinions",
            "Disciplined thinking that bases beliefs on well-founded evidence and logical reasoning",
            "Criticizing everything without offering alternatives",
            "Following the arguments of authority figures"
        ],
        "correct": 1,
        "section": "Socrates and Ancient Philosophy"
    },
    {
        "id": 63,
        "question": "Metaphysics addresses questions about:",
        "options": [
            "How we should treat other people",
            "What we can know about the world",
            "The most general characteristics of existence and reality",
            "How to construct valid arguments"
        ],
        "correct": 2,
        "section": "Socrates and Ancient Philosophy"
    },
    {
        "id": 64,
        "question": "According to the text, reasoning is:",
        "options": [
            "Always based on emotions and feelings",
            "The process of thinking by which we draw conclusions from evidence",
            "Only useful in mathematics and science",
            "Something that should be avoided in philosophy"
        ],
        "correct": 1,
        "section": "Socrates and Ancient Philosophy"
    },
    {
        "id": 65,
        "question": "What makes philosophy valuable according to the text?",
        "options": [
            "It guarantees wealth and success",
            "It helps achieve freedom, builds critical thinking, and cultivates awareness",
            "It provides easy answers to all life's questions",
            "It allows people to avoid making difficult decisions"
        ],
        "correct": 1,
        "section": "Socrates and Ancient Philosophy"
    },
    {
        "id": 66,
        "question": "What was significant about the Pre-Socratic philosophers?",
        "options": [
            "They were the first to rely purely on religious authority",
            "They made the crucial move from mythological to rational explanations",
            "They rejected all forms of reasoning",
            "They focused only on political questions"
        ],
        "correct": 1,
        "section": "Socrates and Ancient Philosophy"
    },
    {
        "id": 67,
        "question": "According to Plato's Phaedo, what does Socrates say the soul resembles?",
        "options": [
            "The body",
            "Water",
            "Something divine, immortal, and intelligible",
            "A material object"
        ],
        "correct": 2,
        "section": "Socrates and Ancient Philosophy"
    },
    {
        "id": 68,
        "question": "According to Plato, what happens to a soul that becomes 'polluted'?",
        "options": [
            "It becomes stronger",
            "It is dragged down to the visible world after death",
            "It immediately dies",
            "It gains wisdom"
        ],
        "correct": 1,
        "section": "Socrates and Ancient Philosophy"
    },
    {
        "id": 69,
        "question": "What is Plato's view on the relationship between soul and body?",
        "options": [
            "They are equal partners",
            "The soul should rule over the body",
            "The body should control the soul",
            "They are identical"
        ],
        "correct": 1,
        "section": "Socrates and Ancient Philosophy"
    },
    {
        "id": 70,
        "question": "According to Aristotle, what is the 'highest end' that humans seek?",
        "options": [
            "Pleasure and wealth",
            "Fame and recognition",
            "Happiness achieved through virtue and reason",
            "Knowledge of the Forms in another world"
        ],
        "correct": 2,
        "section": "Socrates and Ancient Philosophy"
    },
    
    # SECTION 4: HUMAN NATURE AND DARWIN (71-90)
    {
        "id": 71,
        "question": "What is the 'Traditional Western View' of human nature?",
        "options": [
            "Humans are essentially animals with no special properties",
            "Humans are rational beings with immaterial souls designed for a purpose",
            "Humans are purely physical machines",
            "Humans are naturally evil"
        ],
        "correct": 1,
        "section": "Human Nature and Darwin"
    },
    {
        "id": 72,
        "question": "According to the text, what are Darwin's three key ideas?",
        "options": [
            "Evolution, creation, and intelligent design",
            "Variation, struggle for existence, and natural selection",
            "Adaptation, mutation, and survival",
            "Competition, cooperation, and extinction"
        ],
        "correct": 1,
        "section": "Human Nature and Darwin"
    },
    {
        "id": 73,
        "question": "How does Darwin's theory challenge the Traditional Western view?",
        "options": [
            "It proves that souls don't exist",
            "It suggests humans evolved from other animals rather than being specially designed",
            "It shows that reason is useless",
            "It demonstrates that purpose doesn't exist"
        ],
        "correct": 1,
        "section": "Human Nature and Darwin"
    },
    {
        "id": 74,
        "question": "According to the text, what does Darwin say about human mental faculties?",
        "options": [
            "They are completely different from animal faculties",
            "There is no fundamental difference between human and higher mammal mental faculties",
            "Only humans have mental faculties",
            "Mental faculties don't actually exist"
        ],
        "correct": 1,
        "section": "Human Nature and Darwin"
    },
    {
        "id": 75,
        "question": "What does 'natural selection' mean in Darwin's theory?",
        "options": [
            "Humans consciously choose which traits to develop",
            "Nature actively decides which organisms should survive",
            "Favorable variations are preserved and unfavorable ones destroyed through survival pressures",
            "All variations are equally likely to survive"
        ],
        "correct": 2,
        "section": "Human Nature and Darwin"
    },
    {
        "id": 76,
        "question": "According to Thomas Hobbes' materialist view, humans are essentially:",
        "options": [
            "Rational souls temporarily inhabiting physical bodies",
            "Complex physical machines driven by self-interest",
            "Divine beings made in God's image",
            "Naturally good creatures corrupted by society"
        ],
        "correct": 1,
        "section": "Human Nature and Darwin"
    },
    {
        "id": 77,
        "question": "What is 'psychological egoism' as defended by philosophers like
