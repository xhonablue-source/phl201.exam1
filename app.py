import streamlit as st

# Page config
st.set_page_config(page_title="PHL 201 Comprehensive Exam Quiz", page_icon="🧠", layout="wide")

# Initialize session state
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'show_explanation' not in st.session_state:
    st.session_state.show_explanation = {}

# All 120 questions with explanations
questions = [
    # SECTION 1: EPISTEMOLOGY (1-30)
    },
    {
        "id": 105,
        "question": "According to Hegel, how do we become free and independent?",
        "options": [
            "By isolating ourselves from others",
            "Through recognition from others who see us as free and independent",
            "By accumulating wealth and power",
            "Through meditation and inner reflection alone"
        ],
        "correct": 1,
        "section": "Logic and Argumentation",
        "explanation": "Hegel argued we become self-conscious and free through mutual recognition from others. We need others to recognize us as free, autonomous beings. Self-consciousness is inherently social, not purely individual."
    },
    {
        "id": 106,
        "question": "According to Charles Taylor, how is our identity formed?",
        "options": [
            "Through our genes and biology alone",
            "By our own independent choices without influence",
            "Through dialogue and recognition from others, including our culture",
            "Randomly without any pattern"
        ],
        "correct": 2,
        "section": "Logic and Argumentation",
        "explanation": "Taylor argues identity is dialogically formed - shaped through conversations and interactions with others and our culture. We discover who we are through dialogue, not in isolation. Identity is socially constructed."
    },
    {
        "id": 107,
        "question": "How did Aristotle's view of Forms differ from Plato's?",
        "options": [
            "Aristotle rejected the existence of Forms entirely",
            "Aristotle believed Forms exist in the visible things themselves, not in a separate world",
            "Aristotle thought Forms were created by God",
            "Aristotle agreed completely with Plato"
        ],
        "correct": 1,
        "section": "Logic and Argumentation",
        "explanation": "Unlike Plato's transcendent Forms in another realm, Aristotle placed forms/essences within physical objects themselves. The form of 'tree' exists in actual trees, not in a separate world of Forms."
    },
    {
        "id": 108,
        "question": "According to Confucius, what is the key to overcoming political strife?",
        "options": [
            "Strict laws and harsh punishments",
            "Military force and control",
            "Virtue in both rulers and citizens",
            "Economic prosperity alone"
        ],
        "correct": 2,
        "section": "Logic and Argumentation",
        "explanation": "Confucius emphasized virtue ethics - social harmony comes from cultivating virtue in individuals, especially rulers. When rulers are virtuous, citizens follow their example. Virtue, not force, creates stability."
    },
    {
        "id": 109,
        "question": "According to the rationalistic view, what is the essential characteristic of human nature?",
        "options": [
            "Emotion",
            "Physical strength",
            "Reason",
            "Social connection"
        ],
        "correct": 2,
        "section": "Logic and Argumentation",
        "explanation": "Rationalism holds that reason is the defining human characteristic - what distinguishes humans from animals. Humans are essentially 'rational animals.' Reason is our essence and highest faculty."
    },
    {
        "id": 110,
        "question": "What do feminist critics claim about the rationalistic view?",
        "options": [
            "It is completely accurate",
            "It is sexist and biased against women",
            "It needs minor adjustments",
            "It applies only to ancient times"
        ],
        "correct": 1,
        "section": "Logic and Argumentation",
        "explanation": "Feminist philosophers argue the rationalistic view is gendered - it privileges traits historically associated with men (reason) over those associated with women (emotion, care). This reflects and reinforces gender bias."
    },
    {
        "id": 111,
        "question": "What makes consciousness 'subjective'?",
        "options": [
            "It can be measured scientifically",
            "It exists only as experienced by someone and others cannot be aware of it 'from the inside'",
            "It is the same for everyone",
            "It is purely physical"
        ],
        "correct": 1,
        "section": "Logic and Argumentation",
        "explanation": "Consciousness is subjective because it has a first-person perspective - there's 'something it's like' to be you that only you can directly experience. Others can't access your subjective experiences from the inside."
    },
    {
        "id": 112,
        "question": "What is Descartes' view of human nature called?",
        "options": [
            "Monism",
            "Materialism",
            "Dualism",
            "Idealism"
        ],
        "correct": 2,
        "section": "Logic and Argumentation",
        "explanation": "Descartes' view is substance dualism - humans consist of two distinct substances: res cogitans (thinking substance/mind) and res extensa (extended substance/body). Mind and body are fundamentally different."
    },
    {
        "id": 113,
        "question": "Who was the major advocate of behaviorism?",
        "options": [
            "René Descartes",
            "Gilbert Ryle",
            "John Searle",
            "David Chalmers"
        ],
        "correct": 1,
        "section": "Logic and Argumentation",
        "explanation": "Gilbert Ryle defended philosophical behaviorism in 'The Concept of Mind' (1949), arguing that mental states are dispositions to behave in certain ways, not inner immaterial events."
    },
    {
        "id": 114,
        "question": "What did Ryle call Descartes' view of the mind?",
        "options": [
            "The soul theory",
            "The consciousness hypothesis",
            "The dogma of the ghost in the machine",
            "The dualist error"
        ],
        "correct": 2,
        "section": "Logic and Argumentation",
        "explanation": "Ryle criticized Cartesian dualism as 'the dogma of the Ghost in the Machine' - the mistaken idea that there's an immaterial ghost (mind) inhabiting the physical machine (body)."
    },
    {
        "id": 115,
        "question": "What is the main problem with behaviorism according to critics?",
        "options": [
            "It's too complicated",
            "It reduces the mind to observable behavior, leaving out interior consciousness",
            "It contradicts science",
            "It's too old-fashioned"
        ],
        "correct": 1,
        "section": "Logic and Argumentation",
        "explanation": "Critics argue behaviorism ignores or eliminates inner subjective consciousness - the qualitative feel of experiences. It only addresses external behavior, missing the 'what it's like' of mental states."
    },
    {
        "id": 116,
        "question": "What analogy is often used to explain the functionalist view of mind?",
        "options": [
            "Mind is like water",
            "Mind is like a ghost",
            "Mind is like a computer",
            "Mind is like a book"
        ],
        "correct": 2,
        "section": "Logic and Argumentation",
        "explanation": "Functionalists often use the computer analogy: mental states are like software (functional organization) that can be implemented in different hardware (brains, computers, etc.). Function, not physical makeup, defines mind."
    },
    {
        "id": 117,
        "question": "Who developed the identity theory?",
        "options": [
            "Descartes",
            "J.J.C. Smart",
            "Gilbert Ryle",
            "John Locke"
        ],
        "correct": 1,
        "section": "Logic and Argumentation",
        "explanation": "J.J.C. Smart was a major proponent of mind-brain identity theory in the 1950s-60s, arguing that mental states are identical to brain states, not just correlated with them."
    },
    {
        "id": 118,
        "question": "What is John Searle's 'Chinese Room' argument about?",
        "options": [
            "Learning languages",
            "A person following rules can pass the Turing Test without understanding Chinese",
            "Chinese philosophy",
            "Room design"
        ],
        "correct": 1,
        "section": "Logic and Argumentation",
        "explanation": "Searle's Chinese Room argument challenges strong AI: someone can follow rules to respond to Chinese characters (passing the Turing Test) without understanding Chinese. Syntax doesn't guarantee semantics/understanding."
    },
    {
        "id": 119,
        "question": "What is eliminative materialism?",
        "options": [
            "The view that only physical things exist",
            "The view that our ordinary conceptions of mind are false and should be eliminated",
            "The view that we should eliminate the body",
            "The view that consciousness doesn't exist"
        ],
        "correct": 1,
        "section": "Logic and Argumentation",
        "explanation": "Eliminative materialism argues our folk psychology (beliefs, desires, etc.) is a false theory that will be replaced by neuroscience. Mental concepts should be eliminated like outdated scientific theories (phlogiston)."
    },
    {
        "id": 120,
        "question": "Philosophy differs from other fields because it:",
        "options": [
            "Studies ancient texts only",
            "Examines fundamental assumptions other fields take for granted",
            "Requires no evidence",
            "Focuses on practical problems only"
        ],
        "correct": 1,
        "section": "Logic and Argumentation",
        "explanation": "Philosophy is uniquely concerned with examining the fundamental assumptions and concepts that other disciplines take as given. It questions the foundations that other fields build upon."
    }
]

# Display title
st.title("🧠 PHL 201 Comprehensive Exam Quiz - Tutorial Mode")
st.markdown("---")

# Display title
st.title("🧠 PHL 201 Comprehensive Exam Quiz - Tutorial Mode")
st.markdown("---")

# Display instructions
st.markdown("""
### Instructions
- Answer all 120 questions
- **Tutorial Mode**: Get instant feedback after each answer
- See if you're correct and read explanations immediately
- Track your progress as you go
""")

# Progress tracking
total_questions = len(questions)
answered_correctly = sum(1 for q in questions if st.session_state.answers.get(q['id']) == q['correct'])
answered_total = len(st.session_state.answers)

# Summary stats at top
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Questions Answered", f"{answered_total}/{total_questions}")
with col2:
    st.metric("Correct Answers", answered_correctly)
with col3:
    if answered_total > 0:
        percentage = (answered_correctly / answered_total) * 100
        st.metric("Current Score", f"{percentage:.1f}%")
    else:
        st.metric("Current Score", "0%")

st.progress(answered_total / total_questions)
st.markdown("---")

# Display questions by section
current_section = None
for q in questions:
    # Section header
    if q['section'] != current_section:
        current_section = q['section']
        st.markdown(f"## {current_section}")
        st.markdown("---")
    
    # Question container
    with st.container():
        st.markdown(f"### Question {q['id']}")
        st.markdown(f"**{q['question']}**")
        
        # Radio buttons for options
        user_answer = st.radio(
            "Select your answer:",
            options=range(len(q['options'])),
            format_func=lambda x, q=q: q['options'][x],
            key=f"q_{q['id']}",
            index=st.session_state.answers.get(q['id']) if q['id'] in st.session_state.answers else None
        )
        
        # Store answer and show feedback
        if user_answer is not None:
            st.session_state.answers[q['id']] = user_answer
            
            # Show immediate feedback
            if user_answer == q['correct']:
                st.success("✅ Correct!")
            else:
                st.error(f"❌ Incorrect. The correct answer is: **{q['options'][q['correct']]}**")
            
            # Show explanation
            with st.expander("📖 Explanation"):
                st.write(q['explanation'])
        
        st.markdown("---")

# Final summary at bottom
if answered_total == total_questions:
    st.markdown("## 🎉 Quiz Complete!")
    st.balloons()
    
    final_score = (answered_correctly / total_questions) * 100
    
    if final_score >= 90:
        grade = "A"
        message = "Outstanding! You have an excellent grasp of the material!"
    elif final_score >= 80:
        grade = "B"
        message = "Great job! You understand most of the concepts well."
    elif final_score >= 70:
        grade = "C"
        message = "Good work! Review the explanations for questions you missed."
    elif final_score >= 60:
        grade = "D"
        message = "You're getting there. Study the explanations and try again."
    else:
        grade = "F"
        message = "Keep studying! Review all the explanations carefully."
    
    st.success(f"### Final Score: {answered_correctly}/{total_questions} ({final_score:.1f}%) - Grade: {grade}")
    st.info(message)
    
    # Section breakdown
    st.markdown("### Score by Section")
    sections = {}
    for q in questions:
        section = q['section']
        if section not in sections:
            sections[section] = {'correct': 0, 'total': 0}
        sections[section]['total'] += 1
        if st.session_state.answers.get(q['id']) == q['correct']:
            sections[section]['correct'] += 1
    
    for section, data in sections.items():
        percentage = (data['correct'] / data['total']) * 100
        st.write(f"**{section}:** {data['correct']}/{data['total']} ({percentage:.1f}%)") 1,
        "question": "What is epistemology?",
        "options": [
            "The study of being and existence",
            "The study of knowledge and truth",
            "The study of ethics and morality",
            "The study of logic and argumentation"
        ],
        "correct": 1,
        "section": "Epistemology",
        "explanation": "Epistemology is the branch of philosophy concerned with the theory of knowledge - what we can know, how we know it, and what justifies our beliefs as knowledge rather than mere opinion."
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
        "section": "Epistemology",
        "explanation": "The classical (tripartite) definition states that knowledge requires three conditions: (1) belief, (2) truth, and (3) justification. You must believe something, it must be true, and you must have good reasons for believing it."
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
        "section": "Epistemology",
        "explanation": "Edmund Gettier presented cases where someone has a justified true belief but still doesn't seem to have knowledge (due to luck). This challenged the idea that justified true belief is sufficient for knowledge."
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
        "section": "Epistemology",
        "explanation": "Rationalism holds that reason and logical thinking are the primary sources of knowledge, rather than sensory experience. Rationalists like Descartes believed many truths could be known through pure reason alone."
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
        "section": "Epistemology",
        "explanation": "Empiricism holds that knowledge comes primarily from sensory experience and observation. Empiricists like John Locke argued that all knowledge ultimately derives from what we can perceive through our senses."
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
        "section": "Epistemology",
        "explanation": "A priori knowledge can be known through reason alone, without needing sensory experience. Mathematical truths (like 2+2=4) and logical principles are examples of a priori knowledge."
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
        "section": "Epistemology",
        "explanation": "A posteriori knowledge depends on empirical evidence and experience. You can only know 'the sky is blue' or 'water boils at 100°C' by observing the world, not through pure reason."
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
        "section": "Epistemology",
        "explanation": "Philosophical skepticism questions whether we can truly know anything at all. Skeptics raise doubts about the reliability of our senses, reasoning, and sources of information."
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
        "section": "Epistemology",
        "explanation": "Foundationalism argues that some beliefs are 'foundational' - they are self-evident or directly justified and serve as the basis for justifying other beliefs, preventing an infinite regress of justification."
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
        "section": "Epistemology",
        "explanation": "Coherentism holds that beliefs are justified by how well they fit together in a coherent system, rather than resting on foundational beliefs. A belief is justified if it coheres with your other beliefs."
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
        "section": "Epistemology",
        "explanation": "Reliabilism says a belief counts as knowledge if it was formed through a reliable process - one that regularly produces true beliefs. For example, normal vision in good light is reliable, while guessing is not."
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
        "section": "Epistemology",
        "explanation": "Knowledge requires both truth (correspondence to reality) and justification (good reasons). Opinion may lack either truth or proper justification. You can have an opinion without really knowing."
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
        "section": "Epistemology",
        "explanation": "Internalism says that what justifies your beliefs must be things you can be aware of or access through reflection. You should be able to tell, from your own perspective, whether your belief is justified."
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
        "section": "Epistemology",
        "explanation": "Externalism allows that your beliefs can be justified by factors you're not aware of - like the reliability of your perceptual processes or the trustworthiness of your informant, even if you don't know about these factors."
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
        "section": "Epistemology",
        "explanation": "The correspondence theory holds that a statement is true if it corresponds to or matches reality. 'Snow is white' is true if and only if snow actually is white in reality."
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
        "section": "Epistemology",
        "explanation": "The tripartite (three-part) definition says knowledge requires: (1) you must believe it, (2) it must be true, and (3) you must be justified in believing it. All three conditions are necessary."
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
        "section": "Epistemology",
        "explanation": "Fallibilism accepts that we can have knowledge even without absolute certainty. We might be wrong, but that doesn't mean we don't know. Most of our knowledge is fallible but still genuinely knowledge."
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
        "section": "Epistemology",
        "explanation": "The regress problem asks: if every belief needs justification from another belief, don't we get an infinite chain? What stops the regress? Foundationalism and coherentism offer different solutions to this problem."
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
        "section": "Epistemology",
        "explanation": "Virtue epistemology emphasizes intellectual character traits like open-mindedness, intellectual courage, and carefulness. Knowledge comes from exercising these intellectual virtues properly."
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
        "section": "Epistemology",
        "explanation": "Contextualism holds that whether we say someone 'knows' something can depend on the context - the standards for knowledge might be higher in some contexts (like a courtroom) than others (casual conversation)."
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
        "section": "Epistemology",
        "explanation": "The value problem asks why knowledge is better than just having a true belief by luck. What makes the justification valuable? This is a puzzle for many theories of knowledge."
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
        "section": "Epistemology",
        "explanation": "Even if a lucky guess turns out true, it's not knowledge because it lacks proper justification and is accidentally true. Knowledge requires a non-accidental connection between belief and truth."
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
        "section": "Epistemology",
        "explanation": "Precise definitions are crucial in philosophy because vague or ambiguous terms make it impossible to evaluate whether claims are true or false. Clarity enables proper philosophical analysis."
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
        "section": "Epistemology",
        "explanation": "Epistemic circularity happens when you use a way of knowing to justify itself - like using perception to prove perception is reliable, or using reason to prove reason works. This seems problematic but may be unavoidable."
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
        "section": "Epistemology",
        "explanation": "The problem of the criterion asks: to identify truths, we need criteria for truth, but to establish those criteria, we need to already know some truths. Which comes first? This creates a circular problem."
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
        "section": "Epistemology",
        "explanation": "Modal epistemology studies how we can know about what's possible, necessary, or impossible. How do we know that 2+2 must equal 4, or that water could have been distributed differently?"
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
        "section": "Epistemology",
        "explanation": "A philosophical claim is a statement that asserts something about the world - it's declarative (makes a declaration) and has a truth value (it's either true or false). Questions and emotions are not claims."
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
        "section": "Epistemology",
        "explanation": "Vague claims use terms without clear boundaries. 'John is tall' is vague because 'tall' has no precise cutoff. At what exact height does someone become tall? Vagueness makes evaluation difficult."
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
        "section": "Epistemology",
        "explanation": "An ambiguous claim can be interpreted in multiple ways. 'I saw her duck' could mean I saw her lower her head, or I saw the duck that belongs to her. Context usually clarifies which meaning is intended."
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
        "section": "Epistemology",
        "explanation": "To reduce vagueness, provide clear definitions using examples, synonyms, or explicit explanations. Specify what you mean by your terms so others understand the boundaries of your concepts."
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
        "section": "Plato's Theory of Forms",
        "explanation": "Plato believed the physical world we see is an imperfect reflection of a higher reality - the world of Forms. Physical objects are like shadows or copies of perfect, eternal Forms."
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
        "section": "Plato's Theory of Forms",
        "explanation": "Forms are 'more real' because they're eternal (exist forever), unchanging (never decay or alter), and perfect (have no flaws). Physical objects decay, change, and are imperfect copies of Forms."
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
        "section": "Plato's Theory of Forms",
        "explanation": "Physical objects 'participate in' Forms by resembling or imitating them. A beautiful painting participates in the Form of Beauty - it's beautiful because it shares in or resembles that perfect Form."
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
        "section": "Plato's Theory of Forms",
        "explanation": "Plato believed our souls knew the Forms before birth. When we see an imperfect drawn triangle, we recognize it as triangular because our soul remembers the perfect Form of Triangle. This is called recollection or anamnesis."
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
        "section": "Plato's Theory of Forms",
        "explanation": "The Form of the Good is the highest Form - it's what makes all other Forms intelligible and real, like how the sun makes physical things visible. It's the source of truth and reality itself."
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
        "section": "Plato's Theory of Forms",
        "explanation": "Noesis (knowledge of Forms through dialectic reasoning) is the highest level. Below it are: dianoia (mathematical reasoning), pistis (belief about physical objects), and eikasia (imaging/illusion). Noesis grasps ultimate reality."
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
        "section": "Plato's Theory of Forms",
        "explanation": "The Form of Beauty itself is the truest reality. The physical sunset is a copy of Beauty, the photograph is a copy of the copy, making it even further from reality. Forms are the ultimate reality."
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
        "section": "Plato's Theory of Forms",
        "explanation": "Philosopher-kings have escaped the cave and seen the Forms, especially the Form of the Good. Only they understand true reality and can guide society toward justice and truth. They rule reluctantly, out of duty."
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
        "section": "Plato's Theory of Forms",
        "explanation": "Mathematical truths (like perfect circles or triangles) can't be found in the physical world, yet we understand them. Plato explains this through recollection - our souls remember mathematical Forms from before birth."
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
        "section": "Plato's Theory of Forms",
        "explanation": "Plato sees the same structure in both: in a just soul, reason rules spirit and appetite. In a just state, the rational (philosopher-kings) rule the spirited (guardians) and appetitive (producers). Same Form, different scales."
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
        "section": "Plato's Theory of Forms",
        "explanation": "The shadows represent the physical world we perceive through our senses. Like prisoners seeing only shadows, most people mistake sensory experiences for reality, not realizing there's a higher reality (Forms) beyond."
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
        "section": "Plato's Theory of Forms",
        "explanation": "The journey out of the cave represents philosophical education - moving from ignorance to knowledge, from illusion to truth. The sun represents the Form of the Good, which illuminates all true knowledge."
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
        "section": "Plato's Theory of Forms",
        "explanation": "The enlightened philosopher returns out of moral duty to help free others from ignorance. This represents why philosopher-kings must reluctantly leave contemplation to rule - they have an obligation to help others."
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
        "section": "Plato's Theory of Forms",
        "explanation": "In the allegory, prisoners are comfortable with familiar shadows and resist the painful bright light outside. Similarly, people resist philosophical truth because it's difficult and challenges comfortable illusions they're used to."
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
        "section": "Plato's Theory of Forms",
        "explanation": "Just as the sun makes physical things visible, the Form of the Good makes the Forms knowable and gives them reality. It's the ultimate source of truth and being - the highest object of knowledge."
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
        "section": "Plato's Theory of Forms",
        "explanation": "The returned prisoner's duty to free others shows that those who attain knowledge have a moral obligation to help others reach enlightenment. Knowledge brings responsibility, not just privilege."
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
        "section": "Plato's Theory of Forms",
        "explanation": "Just as there are Forms of Triangle and Beauty, there are eternal Forms of moral concepts like Justice, Courage, and the Good. Moral knowledge means grasping these perfect, unchanging moral Forms."
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
        "section": "Plato's Theory of Forms",
        "explanation": "Physical things are less real because they're temporary (come into being and pass away), changing (constantly in flux), and imperfect (flawed copies). Forms are eternal, unchanging, and perfect - thus more 'real.'"
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
        "section": "Plato's Theory of Forms",
        "explanation": "Mathematical truths are universal because they reflect eternal Forms that exist independently of human minds. Anyone with reason can discover these same Forms, which is why mathematics is the same across cultures."
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
        "section": "Plato's Theory of Forms",
        "explanation": "Aristotle argued: if particular humans resemble the Form of Human, we need another Form to explain that resemblance relationship, then another Form for that relationship, etc. - creating an infinite regress of Forms."
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
        "section": "Socrates and Ancient Philosophy",
        "explanation": "Socrates was charged with corrupting the youth (by teaching them to question authority) and impiety (not believing in the gods of Athens). His questioning method threatened traditional beliefs and made him enemies."
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
        "section": "Socrates and Ancient Philosophy",
        "explanation": "Socrates tested the Oracle's claim by questioning supposedly wise people (politicians, poets, craftsmen). He discovered they didn't really know what they claimed to know, while he at least knew that he didn't know."
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
        "section": "Socrates and Ancient Philosophy",
        "explanation": "The Socratic method (elenchus) uses questions to expose contradictions and reveal ignorance. Socrates wanted to show people they didn't truly understand concepts they claimed to know, encouraging intellectual humility."
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
        "section": "Socrates and Ancient Philosophy",
        "explanation": "Socrates argued he had an implicit agreement with Athens' laws. The laws gave him life, education, and protection. Escaping would violate this agreement and harm the legal system. He chose to honor his obligations."
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
        "section": "Socrates and Ancient Philosophy",
        "explanation": "Socrates called himself a 'gadfly' - an annoying insect that stings a lazy horse (Athens) to keep it awake and moving. His questioning was meant to rouse Athens from complacency and make citizens think critically."
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
        "section": "Socrates and Ancient Philosophy",
        "explanation": "Socrates believed that to live well, we must examine our beliefs, values, and actions through philosophical reflection. A life lived without critical self-examination is not truly valuable or worth living."
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
        "section": "Socrates and Ancient Philosophy",
        "explanation": "Socratic wisdom means recognizing the limits of your knowledge. Unlike others who falsely believed they knew, Socrates was wise because he knew he didn't know. This intellectual humility is the starting point for genuine wisdom."
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
        "section": "Socrates and Ancient Philosophy",
        "explanation": "Socrates believed 'virtue is knowledge.' If you truly know what's good, you'll do it. People only do wrong because of ignorance - they don't really understand what's good. No one willingly does evil."
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
        "section": "Socrates and Ancient Philosophy",
        "explanation": "Philosophy comes from Greek 'philos' (love) and 'sophia' (wisdom). Philosophers are 'lovers of wisdom' - they seek wisdom but don't claim to possess it completely, distinguishing them from those who claim to be wise."
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
        "section": "Socrates and Ancient Philosophy",
        "explanation": "Philosophy aims to help you think for yourself by critically examining fundamental beliefs and assumptions. It develops autonomy (self-governance) through rational reflection, not by accepting authority or tradition uncritically."
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
        "section": "Socrates and Ancient Philosophy",
        "explanation": "The three main branches are: epistemology (theory of knowledge), metaphysics (nature of reality), and ethics (moral philosophy). These cover how we know, what exists, and how we should live."
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
        "section": "Socrates and Ancient Philosophy",
        "explanation": "Critical thinking means carefully evaluating claims based on evidence and logic, not emotion or authority. It's disciplined, systematic thinking that distinguishes good reasons from bad reasons for beliefs."
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
        "section": "Socrates and Ancient Philosophy",
        "explanation": "Metaphysics studies the fundamental nature of reality: What exists? What is being? What are space and time? What is causation? It examines the most basic features of existence itself."
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
        "section": "Socrates and Ancient Philosophy",
        "explanation": "Reasoning is the process of moving from evidence (premises) to conclusions through logical thinking. It's how we justify beliefs and evaluate arguments, forming the foundation of rational inquiry."
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
        "section": "Socrates and Ancient Philosophy",
        "explanation": "Philosophy develops intellectual freedom by teaching critical thinking, helps you understand yourself and the world better, and cultivates self-awareness. These are valuable even if they don't lead to material success."
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
        "section": "Socrates and Ancient Philosophy",
        "explanation": "Pre-Socratics (like Thales, Heraclitus, Parmenides) pioneered rational, natural explanations instead of mythological ones. They sought to explain nature through reason and observation rather than stories of gods."
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
        "section": "Socrates and Ancient Philosophy",
        "explanation": "In the Phaedo, Socrates argues the soul is like the Forms - divine, immortal, intelligible (knowable by reason), and unchanging. This contrasts with the body, which is mortal, visible, and changing."
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
        "section": "Socrates and Ancient Philosophy",
        "explanation": "Plato believed that souls overly attached to bodily pleasures become 'polluted' and are dragged back down to the physical world after death. Only purified souls focused on wisdom can ascend to the realm of Forms."
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
        "section": "Socrates and Ancient Philosophy",
        "explanation": "Plato believed the rational soul should rule over the body and its desires, just as reason should rule spirit and appetite in a just soul. The body can distract from philosophical truth if not controlled."
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
        "section": "Socrates and Ancient Philosophy",
        "explanation": "Aristotle argued the highest human good is eudaimonia (happiness/flourishing) achieved through living virtuously according to reason. This differs from Plato's emphasis on escaping to a transcendent realm of Forms."
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
        "section": "Human Nature and Darwin",
        "explanation": "The Traditional Western View (influenced by Greek philosophy and Christianity) sees humans as special: rational, possessing immortal souls, and created with a purpose. This sets humans fundamentally apart from animals."
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
        "section": "Human Nature and Darwin",
        "explanation": "Darwin's theory rests on: (1) variation within species, (2) struggle for existence (competition for limited resources), and (3) natural selection (favorable variations survive and reproduce more)."
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
        "section": "Human Nature and Darwin",
        "explanation": "Darwin challenged the idea that humans were specially created. Evolution suggests humans descended from other animals through natural processes, not divine design. This threatened traditional views of human uniqueness."
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
        "section": "Human Nature and Darwin",
        "explanation": "Darwin argued that human mental abilities differ from animals in degree, not kind. Higher animals show rudimentary reasoning, emotion, and even moral sense - the difference is quantitative, not a fundamental gulf."
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
        "section": "Human Nature and Darwin",
        "explanation": "Natural selection means organisms with advantageous traits are more likely to survive and reproduce, passing those traits to offspring. Over time, favorable variations accumulate while unfavorable ones are eliminated."
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
        "section": "Human Nature and Darwin",
        "explanation": "Hobbes was a materialist who rejected immaterial souls. He viewed humans as physical machines whose behavior is determined by physical causes, primarily self-interest and desire for self-preservation."
    },
    {
        "id": 77,
        "question": "What is 'psychological egoism' as defended by philosophers like Hobbes?",
        "options": [
            "The view that people should be selfish",
            "The descriptive claim that all human actions are ultimately motivated by self-interest",
            "The idea that psychology is the most important science",
            "The belief that egos are psychological constructs"
        ],
        "correct": 1,
        "section": "Human Nature and Darwin",
        "explanation": "Psychological egoism is a descriptive theory claiming that all human actions, even apparently altruistic ones, are ultimately motivated by self-interest. It's about what humans actually do, not what they should do."
    },
    {
        "id": 78,
        "question": "How does the Judeo-Christian view of human nature differ from Greek rationalism?",
        "options": [
            "It denies that humans have rational capacities",
            "It adds the concept of humans being made in God's image with moral will",
            "It rejects the idea that humans have souls",
            "It claims humans are naturally perfect"
        ],
        "correct": 1,
        "section": "Human Nature and Darwin",
        "explanation": "While Greek rationalism emphasized reason, Judeo-Christian thought added: humans are created in God's image (imago Dei), have free will to choose between good and evil, and possess inherent moral worth."
    },
    {
        "id": 79,
        "question": "According to Augustine, what are the three disordered desires that corrupt human will?",
        "options": [
            "Reason, spirit, and appetite",
            "Lust, curiosity, and pride",
            "Faith, hope, and charity",
            "Mind, body, and soul"
        ],
        "correct": 1,
        "section": "Human Nature and Darwin",
        "explanation": "Augustine identified three sinful desires: lust (disordered physical desire), curiosity (disordered desire for knowledge), and pride (disordered self-love). These corrupt the will and lead humans away from God."
    },
    {
        "id": 80,
        "question": "What is the mind-body problem?",
        "options": [
            "How to keep both mind and body healthy",
            "How mind and body can be so different yet interact",
            "Whether the brain is part of the body",
            "Why we have both thoughts and feelings"
        ],
        "correct": 1,
        "section": "Human Nature and Darwin",
        "explanation": "The mind-body problem asks: if mind and body are fundamentally different substances (mental vs. physical), how can they causally interact? How can physical events cause mental states and vice versa?"
    },
    {
        "id": 81,
        "question": "What is consciousness according to the text?",
        "options": [
            "The ability to move",
            "Awareness of sensing, feeling, and thinking when awake",
            "Having a brain",
            "The ability to speak"
        ],
        "correct": 1,
        "section": "Human Nature and Darwin",
        "explanation": "Consciousness is your subjective awareness of experiences - sensing, feeling, thinking. It's the 'what it's like' to be you, the inner subjective experience that accompanies mental states."
    },
    {
        "id": 82,
        "question": "What is dualism in philosophy of mind?",
        "options": [
            "The view that there are two gods",
            "The view that humans consist of two different kinds of things: mind and body",
            "The view that there are two types of bodies",
            "The view that consciousness has two parts"
        ],
        "correct": 1,
        "section": "Human Nature and Darwin",
        "explanation": "Dualism holds that reality consists of two fundamentally different substances: mental (mind/soul) and physical (body). The mind is immaterial while the body is material - they're distinct kinds of things."
    },
    {
        "id": 83,
        "question": "Who was the first great philosopher of the modern age to propose a clear version of mind-body dualism?",
        "options": [
            "Plato",
            "Aristotle",
            "René Descartes",
            "David Hume"
        ],
        "correct": 2,
        "section": "Human Nature and Darwin",
        "explanation": "René Descartes (1596-1650) developed modern dualism. While Plato had dualistic ideas, Descartes gave the first clear, systematic modern account of mind-body dualism in his Meditations."
    },
    {
        "id": 84,
        "question": "What famous conclusion did Descartes reach on November 10, 1619?",
        "options": [
            "God exists",
            "The body and mind are separate",
            "I think, therefore I am",
            "Everything is an illusion"
        ],
        "correct": 2,
        "section": "Human Nature and Darwin",
        "explanation": "Descartes reached 'Cogito, ergo sum' (I think, therefore I am). Even if he doubts everything, he cannot doubt that he exists as a thinking thing, because doubting itself is thinking."
    },
    {
        "id": 85,
        "question": "According to Descartes, can you conceive of yourself without a body?",
        "options": [
            "No, it's impossible",
            "Yes, but not without a thinking mind",
            "Only in dreams",
            "Only after death"
        ],
        "correct": 1,
        "section": "Human Nature and Darwin",
        "explanation": "Descartes argued you can conceive of yourself existing without a body (as a disembodied mind), but you cannot conceive of yourself without thinking. This suggests mind is essential to you, body is not."
    },
    {
        "id": 86,
        "question": "What crucial assumption does Descartes make about conceivability?",
        "options": [
            "If you can conceive of one thing without another, they must be different",
            "Conceiving something makes it real",
            "What you cannot conceive doesn't exist",
            "Conceivability proves immortality"
        ],
        "correct": 0,
        "section": "Human Nature and Darwin",
        "explanation": "Descartes assumes: if you can clearly and distinctly conceive X without Y, then X and Y are really distinct substances. Since you can conceive mind without body, they must be different substances."
    },
    {
        "id": 87,
        "question": "What is behaviorism's main claim about the mind?",
        "options": [
            "The mind is a separate substance",
            "The mind is how you behave",
            "The mind doesn't exist",
            "The mind is the soul"
        ],
        "correct": 1,
        "section": "Human Nature and Darwin",
        "explanation": "Behaviorism, defended by Gilbert Ryle, claims mental states are just behavioral dispositions - tendencies to behave in certain ways. 'Mind' refers to patterns of behavior, not an inner immaterial substance."
    },
    {
        "id": 88,
        "question": "What is functionalism's main claim?",
        "options": [
            "The mind is a separate substance",
            "Mental activities can be explained as connections between sensory inputs and behavior outputs",
            "Only behavior matters",
            "The mind is identical to the brain"
        ],
        "correct": 1,
        "section": "Human Nature and Darwin",
        "explanation": "Functionalism defines mental states by their functional role - causal relations between inputs (sensory), other mental states, and outputs (behavior). What matters is function, not physical implementation."
    },
    {
        "id": 89,
        "question": "What is the identity theory of mind?",
        "options": [
            "Mind and body are identical",
            "Mental states are simply identical with states of the brain",
            "All minds are identical",
            "Identity is a mental construct"
        ],
        "correct": 1,
        "section": "Human Nature and Darwin",
        "explanation": "Identity theory (mind-brain identity theory) claims mental states are literally identical to brain states. Pain is identical to C-fiber firing, not just correlated with it. Mental = physical brain states."
    },
    {
        "id": 90,
        "question": "According to David Hume, what is the self?",
        "options": [
            "An immortal soul",
            "Identical to the physical body",
            "A bundle of constantly changing perceptions with no enduring self",
            "Created by God"
        ],
        "correct": 2,
        "section": "Human Nature and Darwin",
        "explanation": "Hume argued there's no permanent self - just a 'bundle' of constantly changing perceptions, sensations, and thoughts. When you introspect, you never find a 'self,' only particular experiences."
    },
    
    # SECTION 5: LOGIC AND ARGUMENTATION (91-120)
    {
        "id": 91,
        "question": "What are the two main components of an argument?",
        "options": [
            "Facts and opinions",
            "Premises and conclusion",
            "Questions and answers",
            "Problems and solutions"
        ],
        "correct": 1,
        "section": "Logic and Argumentation",
        "explanation": "Arguments consist of premises (reasons/evidence) and a conclusion (claim being supported). Premises provide the support, while the conclusion is what the arguer wants you to accept."
    },
    {
        "id": 92,
        "question": "A valid argument is one in which:",
        "options": [
            "The premises are true",
            "The conclusion is true",
            "If the premises are true, the conclusion must be true",
            "Everyone agrees with the conclusion"
        ],
        "correct": 2,
        "section": "Logic and Argumentation",
        "explanation": "Validity concerns logical structure: IF the premises were true, THEN the conclusion would necessarily follow. A valid argument can have false premises, but if premises were true, conclusion must be too."
    },
    {
        "id": 93,
        "question": "A sound argument is:",
        "options": [
            "Any argument that sounds convincing",
            "A valid argument with true premises",
            "An argument everyone accepts",
            "An argument made by an authority"
        ],
        "correct": 1,
        "section": "Logic and Argumentation",
        "explanation": "A sound argument must be both valid (good logical structure) AND have actually true premises. Soundness guarantees the conclusion is true. It's the gold standard for deductive arguments."
    },
    {
        "id": 94,
        "question": "What makes an argument invalid?",
        "options": [
            "False premises",
            "A conclusion that could be false even if the premises are true",
            "An unpopular conclusion",
            "Too many premises"
        ],
        "correct": 1,
        "section": "Logic and Argumentation",
        "explanation": "An argument is invalid when the conclusion doesn't logically follow from the premises - the premises could all be true while the conclusion is still false. Invalidity is about faulty logical structure."
    },
    {
        "id": 95,
        "question": "The difference between deductive and inductive arguments is:",
        "options": [
            "Deductive arguments are longer than inductive ones",
            "Deductive arguments aim for certainty, inductive for probability",
            "Deductive arguments are always true, inductive are always false",
            "There is no difference"
        ],
        "correct": 1,
        "section": "Logic and Argumentation",
        "explanation": "Deductive arguments aim for necessary conclusions (if premises true, conclusion must be true). Inductive arguments aim for probable conclusions (premises make conclusion likely but not certain)."
    },
    {
        "id": 96,
        "question": "What does it mean to 'beg the question' in logic?",
        "options": [
            "To ask a lot of questions",
            "To assume what you're trying to prove (circular reasoning)",
            "To ask politely for something",
            "To raise an important issue"
        ],
        "correct": 1,
        "section": "Logic and Argumentation",
        "explanation": "Begging the question (petitio principii) is circular reasoning - assuming in your premises what you're supposed to prove in your conclusion. The argument goes in a circle rather than providing independent support."
    },
    {
        "id": 97,
        "question": "Philosophical arguments differ from opinions because they:",
        "options": [
            "Are always true",
            "Provide premises to support conclusions",
            "Are popular",
            "Are easy"
        ],
        "correct": 1,
        "section": "Logic and Argumentation",
        "explanation": "Arguments provide reasoned support (premises) for conclusions. Mere opinions lack this rational support. Philosophy requires giving reasons and evidence, not just stating beliefs."
    },
    {
        "id": 98,
        "question": "Theoretical thinking holds that:",
        "options": [
            "Multiple views can be true",
            "If one view is correct, different views must be incorrect",
            "All opinions are equal",
            "Truth is relative"
        ],
        "correct": 1,
        "section": "Logic and Argumentation",
        "explanation": "Theoretical thinking assumes contradictory views can't both be true. If one position is correct about reality, opposing positions must be false. This reflects the law of non-contradiction."
    },
    {
        "id": 99,
        "question": "Anarchic thinking:",
        "options": [
            "Studies different subjects",
            "Accepts multiple valid perspectives while theoretical seeks one correct view",
            "Uses different methods",
            "Is ancient"
        ],
        "correct": 1,
        "section": "Logic and Argumentation",
        "explanation": "Anarchic thinking (in epistemology) allows that different perspectives might all be valid or that there's no single correct view. This contrasts with theoretical thinking which seeks one true answer."
    },
    {
        "id": 100,
        "question": "The law of non-contradiction states:",
        "options": [
            "Everything contradicts",
            "Something cannot both be and not be in the same respect at the same time",
            "All contradictions are true",
            "Logic is impossible"
        ],
        "correct": 1,
        "section": "Logic and Argumentation",
        "explanation": "The law of non-contradiction is fundamental to logic: A proposition and its negation cannot both be true at the same time in the same respect. X cannot be both true and false simultaneously."
    },
    {
        "id": 101,
        "question": "According to Sartre, what does human freedom imply about our choices?",
        "options": [
            "We are free to choose but not responsible for outcomes",
            "When we choose, we imply everyone should choose the same",
            "Freedom means we can avoid making choices",
            "Our choices are determined by God"
        ],
        "correct": 1,
        "section": "Logic and Argumentation",
        "explanation": "Sartre argued that in choosing for ourselves, we're implicitly choosing for all humanity - declaring what humans should be. Our choices reflect what we think is valuable, making them universal prescriptions."
    },
    {
        "id": 102,
        "question": "According to Sartre, what does 'anguish' mean?",
        "options": [
            "Physical pain from difficult decisions",
            "Fear of death",
            "Recognition of our total and deep responsibility when choosing",
            "Uncertainty about the future"
        ],
        "correct": 2,
        "section": "Logic and Argumentation",
        "explanation": "Anguish (angoisse) is the feeling accompanying recognition of our radical freedom and responsibility. We're totally responsible for our choices with no predetermined essence or rules to follow."
    },
    {
        "id": 103,
        "question": "According to John Locke, what makes a person the same over time?",
        "options": [
            "The immaterial soul",
            "The physical body",
            "Memory or consciousness of being that earlier person",
            "Social relationships with others"
        ],
        "correct": 2,
        "section": "Logic and Argumentation",
        "explanation": "Locke argued personal identity consists in continuity of consciousness/memory. You're the same person as yesterday because you remember being that person. Memory, not soul or body, makes personal identity."
    },
    {
        "id": 104,
        "question": "According to Buddhist philosophy, what is the self?",
        "options": [
            "An eternal, unchanging soul",
            "A fleeting, momentary composite that dissolves and changes constantly",
            "Identical to the physical body",
            "A creation of society"
        ],
        "correct": 1,
        "section": "Logic and Argumentation",
        "explanation": "Buddhism teaches 'no-self' (anatta) - there's no permanent, unchanging self. What we call 'self' is a constantly changing collection of physical and mental phenomena, with nothing permanent underneath."
    },
    {
        "id":
