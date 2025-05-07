import streamlit as st
import random

st.set_page_config(page_title="Cybersecurity Quiz", page_icon="🛡️")
st.title("Cybersecurity & Network Fundamentals Quiz")

# ─── Define all questions ─────────────────────────────────────────────────────
questions = [
    {
        "question": "1. Which block cipher mode encrypts each block independently, causing identical plaintext blocks to yield identical ciphertext blocks?",
        "options": ["ECB", "CBC", "CFB"],
        "answer": "ECB",
    },
    {
        "question": "2. In CBC (Cipher Block Chaining) mode, each plaintext block is:",
        "options": [
            "Encrypted directly without modification",
            "XORed with the previous ciphertext block, then encrypted",
            "XORed with the next plaintext block, then encrypted",
        ],
        "answer": "XORed with the previous ciphertext block, then encrypted",
    },
    {
        "question": "3. Packet filtering refers to:",
        "options": [
            "A method of encrypting network packets",
            "A technique for implementing network-based access control",
            "A way to compress packet headers",
        ],
        "answer": "A technique for implementing network-based access control",
    },
    {
        "question": "4. A stateless packet filter:",
        "options": [
            "Tracks connection state before filtering",
            "Makes decisions solely on header fields of each packet",
            "Reassembles packets to inspect full payload",
        ],
        "answer": "Makes decisions solely on header fields of each packet",
    },
    {
        "question": "5. A stateful packet filter:",
        "options": [
            "Ignores connection context",
            "Takes actions based on the connection’s state",
            "Only filters UDP traffic",
        ],
        "answer": "Takes actions based on the connection’s state",
    },
    {
        "question": "6. An Access Control List (ACL) is best described as:",
        "options": [
            "A list of encryption keys",
            "An ordered list of if-then rules for permitting or denying traffic",
            "A database of user passwords",
        ],
        "answer": "An ordered list of if-then rules for permitting or denying traffic",
    },
    {
        "question": "7. An access control system determines:",
        "options": [
            "Which encryption algorithm to use",
            "What rights a subject has over a set of objects",
            "How to route packets across networks",
        ],
        "answer": "What rights a subject has over a set of objects",
    },
    {
        "question": "8. In access control terminology, a “subject” is:",
        "options": [
            "A passive resource",
            "An active entity that performs actions",
            "A cryptographic key"
        ],
        "answer": "An active entity that performs actions",
    },
    {
        "question": "9. An “object” in access control is:",
        "options": [
            "A passive resource",
            "An encryption algorithm",
            "A user credential"
        ],
        "answer": "A passive resource",
    },
    {
        "question": "10. “Rights” in access control refer to:",
        "options": [
            "Algorithms",
            "Actions that can be performed",
            "Network protocols"
        ],
        "answer": "Actions that can be performed",
    },
    {
        "question": "11. Which OWASP Top 10 category was previously known as “Sensitive Data Exposure”?",
        "options": [
            "Broken Access Control",
            "Cryptographic Failures",
            "Injection"
        ],
        "answer": "Cryptographic Failures",
    },
    {
        "question": "12. Which OWASP Top 10 category focuses on risks related to design flaws?",
        "options": [
            "Insecure Design",
            "Security Misconfiguration",
            "Vulnerable and Outdated Components"
        ],
        "answer": "Insecure Design",
    },
    {
        "question": "13. Snort is:",
        "options": [
            "A commercial firewall",
            "A free/open-source NIPS/NIDS that does protocol analysis, content searching, and matching",
            "A VPN solution"
        ],
        "answer": "A free/open-source NIPS/NIDS that does protocol analysis, content searching, and matching",
    },
    {
        "question": "14. In a Snort rule header, the first field (e.g. “alert”, “log”) is called the:",
        "options": [
            "Action",
            "Protocol",
            "Direction operator",
            "Payload option"
        ],
        "answer": "Action",
    },
    {
        "question": "15. Which syntax uses parentheses around its options list?",
        "options": [
            "Firewall rule syntax",
            "Snort rule syntax"
        ],
        "answer": "Snort rule syntax",
    },
    {
        "question": "16. Port 80 corresponds to which protocol?",
        "options": ["HTTP", "HTTPS", "SSH"],
        "answer": "HTTP",
    },
    {
        "question": "17. Port 443 corresponds to which protocol?",
        "options": ["FTP", "DNS", "HTTPS"],
        "answer": "HTTPS",
    },
    {
        "question": "18. Port 53 corresponds to which service?",
        "options": ["DNS", "FTP", "SMTP"],
        "answer": "DNS",
    },
    {
        "question": "19. Ports 20 and 21 correspond to which protocol?",
        "options": ["FTP", "SSH", "HTTP"],
        "answer": "FTP",
    },
    {
        "question": "20. Port 22 corresponds to which protocol?",
        "options": ["SSH", "FTP", "HTTP"],
        "answer": "SSH",
    },
    {
        "question": "21. Which firewall rule syntax uses the format `(srcIP, dstIP, proto, srcPort, dstPort, permission)`?",
        "options": ["Firewall rule syntax", "Snort rule syntax"],
        "answer": "Firewall rule syntax",
    },
    {
        "question": "22. Which Snort rule syntax uses square brackets for the header and parentheses for options?",
        "options": ["Firewall rule syntax", "Snort rule syntax"],
        "answer": "Snort rule syntax",
    },
    {
        "question": "23. Snort can operate in which three modes?",
        "options": [
            "Sniffer, packet logger, network intrusion detection",
            "Firewall, IDS, IPS",
            "Router, switch, hub"
        ],
        "answer": "Sniffer, packet logger, network intrusion detection",
    },
]

# ─── Shuffle options once per session ────────────────────────────────────────
if "shuffled_options" not in st.session_state:
    st.session_state.shuffled_options = []
    for q in questions:
        opts = q["options"][:]
        random.shuffle(opts)
        st.session_state.shuffled_options.append(opts)

# ─── Render questions with shuffled choices ──────────────────────────────────
user_answers = {}
for idx, q in enumerate(questions):
    user_answers[idx] = st.radio(
        q["question"],
        st.session_state.shuffled_options[idx],
        key=f"q{idx}"
    )

# ─── Submission & Scoring ────────────────────────────────────────────────────
if st.button("Submit"):
    total = len(questions)
    correct = 0
    wrong = []

    for idx, q in enumerate(questions):
        if user_answers[idx] == q["answer"]:
            correct += 1
        else:
            wrong.append((q["question"], user_answers[idx], q["answer"]))

    st.markdown(f"## Your Score: {correct} / {total}")

    if wrong:
        st.markdown("### Review Your Incorrect Answers:")
        for ques, you, right in wrong:
            st.write(f"**{ques}**")
            st.write(f"- Your answer: {you}")
            st.write(f"- Correct answer: {right}")
    else:
        st.success("🎉 Perfect score! Well done.")
