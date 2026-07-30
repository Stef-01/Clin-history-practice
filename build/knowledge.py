"""Knowledge base for generating timed history/exam practice cards.

Two layers:
  1. DIFFERENTIAL_KB - keyword-matched discriminators for named differentials.
     Keys are lower-case substrings matched against the differential text, so
     "pneumonia" also covers "aspiration pneumonia" and "hospital-acquired
     pneumonia". Longer keys win over shorter ones.
  2. SYSTEM_KB - per-system fallbacks used when nothing in layer 1 matches, so
     every differential still yields a usable focused history and examination.

Each entry supplies:
  hx - discriminating questions to ask in the focused block of the 2-min history
  ex - targeted signs to seek in the focused block of the 3-min examination
"""

# ---------------------------------------------------------------------------
# Layer 1: differential-specific discriminators
# ---------------------------------------------------------------------------

DIFFERENTIAL_KB = {

    # --- Cardiovascular -----------------------------------------------------
    "acs": {
        "hx": ["Character, radiation to jaw or arm, and whether pain came on at rest or with exertion",
               "Associated sweating, nausea, vomiting or a sense of impending doom",
               "Prior angina, stents, bypass or a previous identical episode",
               "Cardiac risk factors: smoking, diabetes, hypertension, lipids, family history under 60",
               "Response to GTN and how long the pain has been continuous"],
        "ex": ["Peripheral perfusion, radial-radial and radial-femoral delay, blood pressure in both arms",
               "JVP, apex beat character, new murmur of mitral regurgitation, third or fourth heart sound",
               "Bibasal crackles and any signs of cardiogenic shock",
               "Look for a non-cardiac source: chest wall tenderness, calf swelling, epigastric tenderness"],
    },
    "myocardial infarction": {
        "hx": ["Onset, duration and whether the pain is continuous or has resolved",
               "Radiation, autonomic features, and exertional versus rest onset",
               "Cardiac risk factors and prior revascularisation",
               "Time of symptom onset precisely - it drives reperfusion decisions"],
        "ex": ["Haemodynamic state, both-arm blood pressure, peripheral perfusion",
               "New murmur, third heart sound, raised JVP, pulmonary crackles",
               "Signs of mechanical complication or right ventricular involvement"],
    },
    "angina": {
        "hx": ["Reproducible exertional threshold and prompt relief with rest or GTN",
               "Any recent change in threshold, frequency or rest symptoms (crescendo pattern)",
               "Cardiac risk factors and functional limitation"],
        "ex": ["Blood pressure, heart rate, murmurs of aortic stenosis, signs of heart failure",
               "Peripheral vascular disease as a marker of diffuse atheroma"],
    },
    "aortic dissection": {
        "hx": ["Abrupt, maximal-at-onset tearing pain, and whether it migrated to back or abdomen",
               "Hypertension, connective tissue disease, bicuspid valve, pregnancy, cocaine use",
               "Transient neurological, limb or abdominal ischaemic symptoms"],
        "ex": ["Blood pressure in both arms, pulse deficits, radial-femoral delay",
               "Early diastolic murmur of aortic regurgitation, JVP and signs of tamponade",
               "Focal neurological deficit, limb ischaemia, abdominal tenderness"],
    },
    "pericarditis": {
        "hx": ["Sharp pleuritic pain, worse lying flat, relieved by sitting forward",
               "Recent viral illness, uraemia, autoimmune disease, recent MI or cardiac surgery"],
        "ex": ["Pericardial friction rub with the diaphragm at the left sternal edge, patient leaning forward",
               "JVP, pulsus paradoxus and muffled heart sounds suggesting effusion or tamponade"],
    },
    "tamponade": {
        "hx": ["Progressive breathlessness, presyncope, known effusion, malignancy, recent procedure or trauma",
               "Anticoagulation and any preceding chest pain"],
        "ex": ["Beck triad: hypotension, raised JVP, muffled heart sounds",
               "Pulsus paradoxus, tachycardia, and Kussmaul sign",
               "Cool peripheries and narrow pulse pressure"],
    },
    "heart failure": {
        "hx": ["Exertional breathlessness, orthopnoea, paroxysmal nocturnal dyspnoea and pillow count",
               "Ankle swelling, weight change, and any recent change to diuretic dose",
               "Precipitant: ischaemia, arrhythmia, infection, non-adherence, salt or fluid load"],
        "ex": ["JVP height, displaced apex, third heart sound, murmurs",
               "Bibasal crackles, pleural effusion, hepatomegaly, sacral and ankle oedema",
               "Perfusion and blood pressure to place the patient on the wet/cold axes"],
    },
    "pulmonary oedema": {
        "hx": ["Speed of onset, orthopnoea, frothy or pink sputum, and preceding chest pain or palpitations",
               "Fluid or salt load, missed diuretics, new drugs, dialysis history"],
        "ex": ["Work of breathing, oxygen saturation, ability to speak in sentences",
               "Widespread crackles or wheeze, raised JVP, gallop rhythm",
               "Blood pressure - hypertensive versus cardiogenic shock phenotype"],
    },
    "arrhythmia": {
        "hx": ["Onset and offset - abrupt or gradual; regular or irregular; rate the patient tapped out",
               "Syncope, chest pain or breathlessness during the episode",
               "Triggers: caffeine, alcohol, stimulants, thyroid disease, electrolyte loss",
               "Family history of sudden cardiac death under 40"],
        "ex": ["Pulse rate, rhythm and volume; blood pressure; signs of shock",
               "JVP for cannon a waves, murmurs of structural disease, signs of heart failure",
               "Thyroid status and any goitre"],
    },
    "atrial fibrillation": {
        "hx": ["Palpitation pattern, exercise tolerance, and symptom duration for rate versus rhythm decisions",
               "Alcohol, thyroid disease, sepsis, and prior stroke or TIA",
               "Anticoagulation history and bleeding risk"],
        "ex": ["Irregularly irregular pulse with apex-radial deficit",
               "Signs of heart failure, valvular murmurs, thyroid signs",
               "Focal neurological deficit from embolism"],
    },
    "aortic stenosis": {
        "hx": ["The triad: exertional syncope, angina and breathlessness",
               "Rate of progression and known valve disease"],
        "ex": ["Slow-rising, low-volume pulse and narrow pulse pressure",
               "Ejection systolic murmur radiating to carotids, soft or absent second heart sound",
               "Heaving, non-displaced apex"],
    },
    "endocarditis": {
        "hx": ["Fever duration, night sweats and weight loss over weeks",
               "Prosthetic valve, congenital lesion, injecting drug use, recent dental or invasive procedure",
               "Embolic events: stroke, back pain, painful digits"],
        "ex": ["New or changing murmur, splinter haemorrhages, Osler nodes, Janeway lesions",
               "Splenomegaly, Roth spots on fundoscopy, and vasculitic rash",
               "Peripheral and central embolic signs including focal neurology"],
    },
    "orthostatic hypotension": {
        "hx": ["Symptoms specifically on standing from lying or sitting, and time of day",
               "Antihypertensives, alpha blockers, nitrates, diuretics, antidepressants",
               "Volume loss, autonomic disease, diabetes, Parkinson disease"],
        "ex": ["Lying and standing blood pressure at 1 and 3 minutes",
               "Volume status: mucous membranes, skin turgor, JVP",
               "Autonomic and neurological examination including gait"],
    },
    "vasovagal": {
        "hx": ["Prodrome of nausea, warmth, tunnel vision or sweating; upright posture or a clear trigger",
               "Rapid full recovery without confusion, and witness account of pallor"],
        "ex": ["Lying and standing blood pressure, cardiovascular examination to exclude structural disease",
               "Tongue bite, incontinence or injury pointing away from simple faint"],
    },
    "peripheral vascular": {
        "hx": ["Claudication distance, rest pain, night pain relieved by hanging the leg down",
               "Non-healing ulcer or gangrene, smoking, diabetes"],
        "ex": ["All peripheral pulses, capillary refill, Buerger angle and venous guttering",
               "Ankle-brachial index, skin changes, hair loss, ulcers between toes and over pressure points"],
    },
    "acute limb ischaemia": {
        "hx": ["Time of onset (drives salvageability), embolic source such as AF, prior claudication",
               "Progression of sensory or motor loss"],
        "ex": ["The six Ps: pain, pallor, pulselessness, perishing cold, paraesthesia, paralysis",
               "Compare with the other limb; document sensation and power - loss means threatened limb",
               "Palpate calf compartments for tenseness"],
    },
    "dvt": {
        "hx": ["Unilateral leg swelling and pain, recent immobility, surgery, long travel, malignancy",
               "Hormonal therapy, pregnancy, previous VTE, family history of clot"],
        "ex": ["Calf circumference 10 cm below tibial tuberosity, both legs",
               "Unilateral warmth, erythema, pitting oedema, dilated superficial veins, calf tenderness"],
    },
    "venous insufficiency": {
        "hx": ["Aching worse at the end of the day, relieved by elevation; varicose veins, prior DVT"],
        "ex": ["Haemosiderin staining, lipodermatosclerosis, varicose eczema, gaiter-area ulceration",
               "Pitting oedema improving overnight, and palpable pedal pulses"],
    },

    # --- Respiratory --------------------------------------------------------
    "pe": {
        "hx": ["Sudden pleuritic pain, breathlessness, haemoptysis, presyncope",
               "VTE risk: surgery, immobility, malignancy, pregnancy or postpartum, oestrogen, prior VTE",
               "Leg swelling or calf pain"],
        "ex": ["Respiratory rate, oxygen saturation, heart rate, blood pressure",
               "Raised JVP, loud pulmonary second sound, right ventricular heave",
               "Unilateral calf swelling and tenderness; pleural rub"],
    },
    "pulmonary embol": {
        "hx": ["Sudden pleuritic pain, breathlessness, haemoptysis, presyncope",
               "VTE risk factors and previous thromboembolism",
               "Leg swelling or calf pain"],
        "ex": ["Vital signs including respiratory rate and saturations",
               "Signs of right heart strain: raised JVP, parasternal heave, loud P2",
               "Calf examination for DVT"],
    },
    "pneumonia": {
        "hx": ["Fever, productive cough, sputum colour, pleuritic pain and rigors",
               "Onset over days, sick contacts, aspiration risk, recent hospital or antibiotic exposure",
               "Functional decline and confusion in older patients"],
        "ex": ["Respiratory rate, saturations, temperature, confusion - build the severity score",
               "Focal dullness, bronchial breathing, coarse crackles, increased vocal resonance",
               "Signs of parapneumonic effusion or sepsis"],
    },
    "asthma": {
        "hx": ["Diurnal and seasonal variability, triggers, atopy and family history",
               "Inhaler technique, adherence, reliever use per week, prior ICU or intubation",
               "Best peak flow and today's peak flow"],
        "ex": ["Ability to complete sentences, respiratory rate, heart rate, saturations",
               "Widespread polyphonic expiratory wheeze; a silent chest is life-threatening",
               "Accessory muscle use, tracheal tug, and exhaustion"],
    },
    "copd": {
        "hx": ["Smoking pack-years, baseline exercise tolerance, sputum volume and purulence change",
               "Exacerbation frequency, home oxygen or nebulisers, prior ventilation",
               "MRC dyspnoea grade"],
        "ex": ["Pursed-lip breathing, hyperexpansion, reduced cricosternal distance",
               "Quiet breath sounds, prolonged expiration, wheeze, CO2 retention flap",
               "Cor pulmonale: raised JVP, peripheral oedema"],
    },
    "pneumothorax": {
        "hx": ["Sudden pleuritic pain and breathlessness at rest; tall thin build or known lung disease",
               "Trauma, recent procedure, and any previous pneumothorax"],
        "ex": ["Tracheal deviation, hyper-resonance, absent breath sounds, reduced expansion",
               "Haemodynamic compromise indicating tension - treat before imaging"],
    },
    "pleural effusion": {
        "hx": ["Progressive breathlessness, orthopnoea, fever, weight loss, asbestos exposure",
               "Cardiac, hepatic and renal comorbidity suggesting a transudate"],
        "ex": ["Stony dull percussion, reduced breath sounds and reduced vocal resonance at the base",
               "Tracheal deviation away in large effusions; look for the cause - JVP, ascites, lymph nodes"],
    },
    "bronchiectasis": {
        "hx": ["Chronic daily sputum production, volume in cups, recurrent infections, haemoptysis",
               "Childhood infection, cystic fibrosis, immunodeficiency, prior TB"],
        "ex": ["Coarse inspiratory crackles that shift with coughing, clubbing",
               "Sputum pot inspection and nutritional state"],
    },
    "tb": {
        "hx": ["Cough over three weeks, night sweats, weight loss, haemoptysis",
               "Country of birth, travel, contacts, incarceration, HIV, immunosuppression"],
        "ex": ["Cachexia, lymphadenopathy, upper zone crackles",
               "Extrapulmonary sites: spine, joints, skin, abdomen, central nervous system"],
    },
    "lung cancer": {
        "hx": ["Weight loss, haemoptysis, hoarseness, persistent cough or a changed chronic cough",
               "Smoking and asbestos exposure; bone pain, headache, seizures suggesting spread"],
        "ex": ["Clubbing, cachexia, supraclavicular and cervical lymph nodes",
               "Horner syndrome, SVC obstruction, monophonic wheeze, collapse or effusion signs",
               "Hepatomegaly, bony tenderness, focal neurology"],
    },
    "interstitial lung": {
        "hx": ["Insidious exertional breathlessness and dry cough over months",
               "Occupational, avian, mould and drug exposures; connective tissue disease symptoms"],
        "ex": ["Fine bibasal end-inspiratory Velcro crackles, clubbing",
               "Signs of connective tissue disease: sclerodactyly, rash, arthropathy"],
    },
    "pulmonary hypertension": {
        "hx": ["Exertional breathlessness and syncope; underlying lung, cardiac or connective tissue disease"],
        "ex": ["Raised JVP with prominent a wave, parasternal heave, loud P2, tricuspid regurgitation murmur",
               "Peripheral oedema and hepatomegaly"],
    },

    # --- Gastrointestinal / hepatobiliary -----------------------------------
    "appendicitis": {
        "hx": ["Periumbilical pain migrating to the right iliac fossa over hours",
               "Anorexia, nausea, low-grade fever; pain worse on movement or coughing",
               "In women, always take a menstrual and sexual history to consider ectopic and PID"],
        "ex": ["Point tenderness at McBurney point, guarding, percussion tenderness, Rovsing sign",
               "Psoas and obturator signs for a retrocaecal or pelvic appendix",
               "Temperature and observe how the patient moves onto the couch"],
    },
    "cholecystitis": {
        "hx": ["Right upper quadrant pain after fatty food, radiating to the right shoulder tip",
               "Duration over 6 hours with fever distinguishes it from biliary colic",
               "Previous gallstones, jaundice, dark urine, pale stool"],
        "ex": ["Murphy sign - arrest of inspiration on right upper quadrant palpation",
               "Fever, jaundice and right upper quadrant mass",
               "Charcot triad if ascending cholangitis is possible"],
    },
    "cholangitis": {
        "hx": ["Fever with rigors, jaundice and right upper quadrant pain; recent ERCP or known stones",
               "Confusion and hypotension indicate Reynolds pentad"],
        "ex": ["Jaundice, right upper quadrant tenderness, fever, haemodynamic state",
               "Sepsis assessment and mental state"],
    },
    "pancreatitis": {
        "hx": ["Severe epigastric pain boring through to the back, relieved by sitting forward",
               "Alcohol intake, gallstones, recent ERCP, triglycerides, drugs",
               "Persistent vomiting and inability to keep fluids down"],
        "ex": ["Epigastric tenderness out of proportion to findings, guarding, absent bowel sounds",
               "Cullen and Grey Turner signs, jaundice",
               "Systemic severity: tachycardia, hypotension, hypoxia, oliguria"],
    },
    "perforation": {
        "hx": ["Sudden severe generalised pain, unable to move; NSAID or steroid use, known ulcer",
               "Preceding obstruction, diverticular disease or recent instrumentation"],
        "ex": ["Rigid, board-like abdomen with generalised guarding and rebound",
               "Absent bowel sounds, loss of liver dullness",
               "Signs of shock and sepsis"],
    },
    "bowel obstruction": {
        "hx": ["Colicky pain, vomiting, distension, absolute constipation - and the order they appeared",
               "Previous abdominal surgery, hernia, malignancy, change in bowel habit"],
        "ex": ["Distension, tympanic percussion, high-pitched or absent bowel sounds",
               "Examine every hernial orifice and the scars; rectal examination for an empty rectum or mass",
               "Localised tenderness suggesting strangulation"],
    },
    "diverticulitis": {
        "hx": ["Left iliac fossa pain, fever, altered bowel habit; previous similar episodes",
               "Rectal bleeding, pneumaturia or faecaluria suggesting fistula"],
        "ex": ["Left iliac fossa tenderness and guarding, mass or fullness",
               "Localised versus generalised peritonism, fever, rectal examination"],
    },
    "peptic ulcer": {
        "hx": ["Epigastric pain related to meals, night waking, relief with antacids",
               "NSAIDs, aspirin, steroids, alcohol, H. pylori history",
               "Melaena, haematemesis, weight loss"],
        "ex": ["Epigastric tenderness, signs of anaemia, evidence of bleeding on rectal examination",
               "Peritonism suggesting perforation"],
    },
    "gord": {
        "hx": ["Burning retrosternal discomfort after meals or lying flat, acid regurgitation, water brash",
               "Response to acid suppression; alarm features: dysphagia, weight loss, anaemia, vomiting"],
        "ex": ["Usually normal - document the absence of alarm signs and epigastric tenderness",
               "Weight, anaemia, supraclavicular nodes"],
    },
    "gastroenteritis": {
        "hx": ["Vomiting and diarrhoea onset, stool frequency, blood or mucus",
               "Food, travel, contacts, recent antibiotics",
               "Fluid intake and urine output"],
        "ex": ["Volume status: mucous membranes, capillary refill, postural blood pressure",
               "Soft abdomen with generalised discomfort but no peritonism",
               "Temperature and signs of systemic infection"],
    },
    "inflammatory bowel": {
        "hx": ["Chronic diarrhoea with blood or mucus, nocturnal symptoms, urgency and tenesmus",
               "Weight loss, mouth ulcers, eye and joint symptoms, perianal disease",
               "Family history and smoking status"],
        "ex": ["Abdominal tenderness or mass, perianal inspection for tags, fissures and fistulae",
               "Extraintestinal signs: erythema nodosum, pyoderma, uveitis, arthritis",
               "Nutritional state and anaemia"],
    },
    "coeliac": {
        "hx": ["Bloating, steatorrhoea, weight loss and their relation to gluten; iron deficiency",
               "Family history and associated autoimmune disease"],
        "ex": ["Nutritional state, angular stomatitis, glossitis, dermatitis herpetiformis",
               "Signs of anaemia and osteomalacia"],
    },
    "irritable bowel": {
        "hx": ["Pain relieved by defaecation, stool form and frequency change, bloating",
               "Symptom duration over months without alarm features; stress relationship"],
        "ex": ["Non-specific abdominal tenderness with a normal examination otherwise",
               "Actively document the absence of masses, weight loss and anaemia"],
    },
    "variceal": {
        "hx": ["Volume and frequency of haematemesis or melaena; alcohol and liver disease history",
               "Previous variceal bleed, banding or beta blockade"],
        "ex": ["Haemodynamic state first: heart rate, blood pressure, postural drop",
               "Stigmata of chronic liver disease, ascites, splenomegaly, encephalopathy grade",
               "Rectal examination for melaena"],
    },
    "cirrhosis": {
        "hx": ["Alcohol, viral hepatitis risk, metabolic syndrome, drugs; decompensation events",
               "Confusion, abdominal swelling, bleeding, jaundice"],
        "ex": ["Peripheral stigmata: spider naevi, palmar erythema, gynaecomastia, Dupuytren, clubbing",
               "Ascites by shifting dullness, splenomegaly, caput medusae",
               "Asterixis, jaundice and mental state"],
    },
    "hepatitis": {
        "hx": ["Jaundice, dark urine, pale stool, right upper quadrant ache, fatigue",
               "Travel, injecting drugs, transfusion, sexual history, paracetamol and herbal medicines",
               "Alcohol quantified in standard drinks"],
        "ex": ["Jaundice, tender hepatomegaly, signs of chronic liver disease",
               "Encephalopathy and asterixis indicating acute liver failure"],
    },
    "ascites": {
        "hx": ["Rate of abdominal swelling, weight change, breathlessness, fever or abdominal pain",
               "Liver disease, heart failure, malignancy, tuberculosis"],
        "ex": ["Shifting dullness and fluid thrill, flank fullness",
               "Signs of chronic liver disease, JVP for a cardiac cause, lymph nodes for malignancy",
               "Tenderness suggesting spontaneous bacterial peritonitis"],
    },
    "mesenteric ischaemia": {
        "hx": ["Pain grossly out of proportion to examination findings; AF or vascular disease",
               "Food fear and weight loss in the chronic form"],
        "ex": ["Soft abdomen despite severe pain early, then peritonism late",
               "Irregular pulse, vascular bruits, and signs of shock"],
    },
    "aaa": {
        "hx": ["Abrupt abdominal or back pain with collapse; known aneurysm, hypertension, smoking"],
        "ex": ["Expansile pulsatile mass above the umbilicus, femoral pulses",
               "Haemodynamic state; do not delay imaging or theatre for a complete examination"],
    },

    # --- Renal / urological -------------------------------------------------
    "uti": {
        "hx": ["Dysuria, frequency, urgency, suprapubic pain, haematuria, offensive urine",
               "Fever, loin pain or rigors suggesting upper tract involvement",
               "Catheter, recent instrumentation, previous resistant organisms, pregnancy"],
        "ex": ["Temperature, suprapubic tenderness, loin and renal angle tenderness",
               "Palpable bladder, catheter and drainage inspection",
               "Confusion and haemodynamic state in older patients"],
    },
    "pyelonephritis": {
        "hx": ["Fever with rigors, loin pain, vomiting, preceding lower urinary tract symptoms",
               "Stones, obstruction, pregnancy, diabetes, immunosuppression"],
        "ex": ["Renal angle tenderness, fever, sepsis assessment",
               "Palpable bladder or hydronephrosis and volume status"],
    },
    "renal colic": {
        "hx": ["Loin-to-groin colicky pain, unable to lie still, nausea and vomiting",
               "Haematuria, previous stones, fluid intake, family history",
               "Fever indicating an infected obstructed system - a urological emergency"],
        "ex": ["Restless, writhing patient; renal angle tenderness with a soft abdomen",
               "Temperature and haemodynamic state; palpate for an aneurysm as a mimic",
               "Testicular examination in men"],
    },
    "acute kidney injury": {
        "hx": ["Urine output trend, fluid losses, and new drugs including NSAIDs, ACE inhibitors, contrast",
               "Obstructive symptoms, sepsis, and baseline renal function"],
        "ex": ["Volume status: JVP, postural blood pressure, mucous membranes, oedema",
               "Palpable bladder and bladder scan; renal angle tenderness",
               "Uraemic features: pericardial rub, asterixis, confusion"],
    },
    "urinary retention": {
        "hx": ["Ability to pass urine, prostatic symptoms, constipation, new anticholinergics or opioids",
               "Back pain, saddle anaesthesia or leg weakness suggesting cauda equina"],
        "ex": ["Palpable, dull, tender suprapubic bladder confirmed with a bladder scan",
               "Digital rectal examination for prostate size and anal tone",
               "Perineal sensation and lower limb neurology"],
    },
    "testicular torsion": {
        "hx": ["Sudden severe testicular pain, often waking from sleep; nausea and vomiting; age under 25",
               "Previous similar self-resolving episodes; time of onset drives salvage"],
        "ex": ["High-riding, transversely lying, exquisitely tender testis",
               "Absent cremasteric reflex; no relief on elevation (negative Prehn sign)",
               "Do not delay urological referral to complete the examination"],
    },
    "epididymo-orchitis": {
        "hx": ["Gradual onset over days, dysuria or urethral discharge, sexual history",
               "Fever and lower urinary tract symptoms in older men"],
        "ex": ["Tender, swollen epididymis with relief on elevation (positive Prehn sign)",
               "Preserved cremasteric reflex, erythematous scrotal skin, fever"],
    },
    "bph": {
        "hx": ["Storage and voiding symptoms: hesitancy, poor stream, terminal dribble, nocturia",
               "Impact on quality of life, retention episodes, haematuria"],
        "ex": ["Smooth, enlarged, non-tender prostate on digital rectal examination",
               "Palpable bladder and abdominal examination"],
    },
    "prostate cancer": {
        "hx": ["Voiding symptoms, haematuria, bone pain, weight loss; family history"],
        "ex": ["Hard, irregular, craggy prostate with loss of the median sulcus",
               "Bony tenderness, particularly the spine, and neurological examination for cord compression"],
    },
    "nephrotic": {
        "hx": ["Frothy urine, periorbital and peripheral oedema, weight gain",
               "Diabetes, autoimmune disease, drugs, infection, malignancy"],
        "ex": ["Periorbital, peripheral and sacral oedema; ascites and pleural effusions",
               "Blood pressure and volume status; signs of thrombosis"],
    },
    "glomerulonephritis": {
        "hx": ["Cola-coloured urine, oedema, recent sore throat or skin infection",
               "Haemoptysis, rash, joint pain suggesting systemic vasculitis"],
        "ex": ["Hypertension, oedema, volume overload",
               "Rash, joint swelling, and respiratory examination for pulmonary-renal syndrome"],
    },

    # --- Endocrine / metabolic ---------------------------------------------
    "diabetes": {
        "hx": ["Polyuria, polydipsia, weight loss, blurred vision and their time course",
               "Glucose monitoring, insulin or oral agents, adherence, hypoglycaemia awareness",
               "Complication screening: feet, eyes, kidneys, cardiovascular events"],
        "ex": ["Hydration, capillary glucose, ketones, and the smell of ketones on the breath",
               "Foot examination: pulses, monofilament sensation, ulcers, deformity",
               "Injection sites for lipohypertrophy, blood pressure, fundoscopy"],
    },
    "dka": {
        "hx": ["Precipitant: infection, missed insulin, new diagnosis, myocardial infarction, steroids",
               "Vomiting, abdominal pain, breathlessness, drowsiness"],
        "ex": ["Kussmaul respiration, ketotic breath, dehydration, conscious level",
               "Capillary glucose and ketones at the bedside",
               "Search for the precipitant: chest, abdomen, skin, feet"],
    },
    "hypoglycaemia": {
        "hx": ["Insulin or sulfonylurea use, missed meals, alcohol, exercise, renal impairment",
               "Autonomic warning symptoms and whether awareness is preserved",
               "Speed of recovery after glucose"],
        "ex": ["Capillary glucose before anything else; conscious level and GCS",
               "Sweating, tremor, tachycardia; focal neurology can mimic stroke"],
    },
    "hyperthyroid": {
        "hx": ["Heat intolerance, weight loss with good appetite, palpitations, anxiety, loose stools",
               "Amiodarone, iodine contrast, recent pregnancy; eye symptoms"],
        "ex": ["Fine tremor, warm sweaty palms, tachycardia or AF, lid lag and lid retraction",
               "Goitre with bruit, thyroid eye signs, proximal myopathy, brisk reflexes",
               "Pretibial myxoedema and thyroid acropachy"],
    },
    "hypothyroid": {
        "hx": ["Cold intolerance, weight gain, fatigue, constipation, low mood, menorrhagia",
               "Previous thyroid surgery or radioiodine, lithium or amiodarone, family history"],
        "ex": ["Dry coarse skin, hair loss, periorbital puffiness, bradycardia",
               "Slow-relaxing ankle reflexes, goitre, non-pitting oedema"],
    },
    "adrenal": {
        "hx": ["Fatigue, weight loss, dizziness on standing, salt craving, pigmentation",
               "Steroid use and any abrupt cessation; intercurrent illness"],
        "ex": ["Postural hypotension, buccal and palmar crease pigmentation",
               "Volume status, and Cushingoid features if excess is suspected"],
    },
    "cushing": {
        "hx": ["Weight gain with thin limbs, easy bruising, mood change, proximal weakness",
               "Exogenous steroid exposure including inhaled, topical and injected"],
        "ex": ["Moon face, interscapular fat pad, purple striae, thin skin, bruising",
               "Proximal myopathy tested by standing from a chair; blood pressure and glucose"],
    },
    "hypercalcaemia": {
        "hx": ["Bones, stones, abdominal groans and psychic moans; thirst and polyuria",
               "Malignancy, thiazides, lithium, vitamin D and calcium supplements"],
        "ex": ["Hydration status, conscious level, abdominal examination",
               "Look for an underlying malignancy: breast, chest, lymph nodes, bones"],
    },
    "hyponatraemia": {
        "hx": ["Fluid intake including beer and tea patterns, diuretics, SSRIs, carbamazepine",
               "Vomiting, diarrhoea, and any headache, nausea, confusion or seizure"],
        "ex": ["Volume status is the pivotal assessment: JVP, postural blood pressure, oedema, mucous membranes",
               "Conscious level and neurological examination"],
    },

    # --- Neurological -------------------------------------------------------
    "stroke": {
        "hx": ["Exact time last known well - it determines thrombolysis and thrombectomy eligibility",
               "Deficit onset (abrupt), progression, and whether symptoms are negative or positive",
               "AF, hypertension, diabetes, smoking, prior stroke or TIA, anticoagulants",
               "Seizure, trauma or hypoglycaemia as stroke mimics"],
        "ex": ["Capillary glucose first, then a structured NIHSS-style deficit assessment",
               "Speech, visual fields, facial and limb power, sensation, coordination, neglect",
               "Blood pressure, heart rhythm, carotid bruits, swallow screen before anything oral"],
    },
    "tia": {
        "hx": ["Complete resolution and duration; deficit character; carotid or vertebrobasilar territory",
               "Amaurosis fugax, and cardiovascular risk factors for the risk score"],
        "ex": ["Full neurological examination to confirm resolution",
               "Pulse for AF, blood pressure, carotid bruits, fundoscopy"],
    },
    "subarachnoid": {
        "hx": ["Thunderclap headache maximal within seconds; the worst headache ever",
               "Neck stiffness, photophobia, vomiting, transient loss of consciousness, seizure",
               "Exertion or straining at onset; family history, polycystic kidney disease"],
        "ex": ["Conscious level, neck stiffness, photophobia",
               "Fundoscopy for subhyaloid haemorrhage and papilloedema",
               "Focal deficits including third nerve palsy, and blood pressure"],
    },
    "meningitis": {
        "hx": ["Fever, headache, neck stiffness, photophobia, rash, and rate of progression over hours",
               "Confusion, seizure, recent ENT infection, immunosuppression, travel, vaccination"],
        "ex": ["Non-blanching rash with a glass test - look everywhere including soles and conjunctivae",
               "Neck stiffness, Kernig and Brudzinski signs, conscious level",
               "Focal neurology and papilloedema before lumbar puncture"],
    },
    "encephalitis": {
        "hx": ["Altered behaviour, personality change or confusion with fever; seizures",
               "Cold sores, travel, animal or mosquito exposure, immunosuppression"],
        "ex": ["Mental state and cognition, conscious level",
               "Focal neurology, particularly temporal lobe signs; fever; rash"],
    },
    "seizure": {
        "hx": ["A witness account is essential: what happened before, during and after",
               "Aura, duration, limb movements, eye deviation, tongue bite, incontinence",
               "Post-ictal confusion or drowsiness and how long it lasted",
               "Sleep deprivation, alcohol, drugs, missed anti-epileptics, head injury"],
        "ex": ["Lateral tongue bite, injuries, incontinence, conscious level and post-ictal state",
               "Capillary glucose, temperature, focal neurology including Todd paresis",
               "Signs of meningism or raised intracranial pressure"],
    },
    "migraine": {
        "hx": ["Unilateral throbbing headache with nausea, photophobia, phonophobia; aura",
               "Duration 4-72 hours, prior identical episodes, triggers, relief in a dark room",
               "Analgesic frequency for medication overuse"],
        "ex": ["Normal neurological examination is the expectation - document it",
               "Fundoscopy, visual fields, and blood pressure to exclude secondary causes"],
    },
    "temporal arteritis": {
        "hx": ["New headache over 50, scalp tenderness, jaw claudication, visual loss",
               "Polymyalgic shoulder and hip girdle stiffness, systemic symptoms"],
        "ex": ["Thickened, tender, pulseless temporal artery",
               "Visual acuity, fields, relative afferent pupillary defect, fundoscopy",
               "Proximal girdle tenderness and power"],
    },
    "raised intracranial pressure": {
        "hx": ["Headache worse on waking, lying flat, coughing or straining; vomiting; visual obscurations",
               "Progressive focal deficit, seizure, personality change; malignancy history"],
        "ex": ["Papilloedema on fundoscopy, visual acuity and fields",
               "Conscious level, pupils, sixth nerve palsy as a false localising sign",
               "Cushing response: hypertension with bradycardia"],
    },
    "guillain": {
        "hx": ["Ascending symmetrical weakness over days, preceded by diarrhoeal or respiratory illness",
               "Sensory symptoms, back pain, and any breathing or swallowing difficulty"],
        "ex": ["Symmetrical flaccid weakness with areflexia; ascending sensory level",
               "Forced vital capacity at the bedside - repeat it; bulbar and facial weakness",
               "Autonomic instability in pulse and blood pressure"],
    },
    "multiple sclerosis": {
        "hx": ["Previous episodes separated in time and anatomical site; optic neuritis, sensory symptoms",
               "Heat sensitivity (Uhthoff), Lhermitte phenomenon, bladder symptoms, fatigue"],
        "ex": ["Visual acuity, colour vision, relative afferent pupillary defect, internuclear ophthalmoplegia",
               "Upper motor neurone signs, cerebellar signs, sensory level, gait"],
    },
    "parkinson": {
        "hx": ["Tremor at rest, slowness, stiffness, micrographia, reduced arm swing; asymmetry at onset",
               "Falls, hallucinations, REM sleep behaviour, constipation, anosmia; drug history for neuroleptics"],
        "ex": ["Resting pill-rolling tremor, cogwheel rigidity, bradykinesia on repetitive movements",
               "Hypomimia, hypophonia, shuffling festinant gait, reduced arm swing, postural instability",
               "Eye movements to screen for progressive supranuclear palsy"],
    },
    "delirium": {
        "hx": ["Acute fluctuating course over hours to days with inattention - collateral history essential",
               "Precipitants: infection, drugs, pain, retention, constipation, withdrawal, metabolic upset",
               "Baseline cognition and function before this illness"],
        "ex": ["Attention testing, conscious level, and a formal delirium screen",
               "Full septic screen, hydration, bladder and bowel, drug chart review",
               "Neurological examination for focal signs"],
    },
    "dementia": {
        "hx": ["Insidious progressive decline over months with a collateral history",
               "Memory, language, executive and visuospatial domains; functional impact on daily activities",
               "Vascular risk, alcohol, mood, and the pattern of onset"],
        "ex": ["Cognitive screening tool, mood assessment",
               "Focal neurology, gait, parkinsonism, primitive reflexes",
               "Signs of reversible causes: thyroid, B12, hearing and vision"],
    },
    "cauda equina": {
        "hx": ["Bilateral leg symptoms, saddle numbness, bladder or bowel dysfunction, sexual dysfunction",
               "Time of onset of urinary symptoms; back pain history and red flags"],
        "ex": ["Perianal sensation, anal tone and voluntary squeeze, post-void bladder scan",
               "Lower limb power, sensation and reflexes; straight leg raise",
               "Do not delay urgent MRI to complete the examination"],
    },
    "spinal cord compression": {
        "hx": ["Progressive weakness, sensory level, band-like pain, bladder and bowel change",
               "Known malignancy, weight loss, night pain, fever, injecting drug use"],
        "ex": ["Sensory level mapped on the trunk, upper motor neurone signs below the lesion",
               "Spinal percussion tenderness, gait, perianal sensation and anal tone"],
    },
    "peripheral neuropathy": {
        "hx": ["Glove-and-stocking distribution, burning or numbness, symmetry, time course",
               "Diabetes, alcohol, B12, chemotherapy, renal disease, family history"],
        "ex": ["Distal sensory loss with a defined level, absent ankle reflexes",
               "Vibration and proprioception, monofilament, Romberg and gait",
               "Foot inspection for ulcers and deformity"],
    },
    "radiculopathy": {
        "hx": ["Dermatomal pain radiating below the knee or into the hand, worse on coughing",
               "Weakness and numbness in a myotomal pattern; red flags for cauda equina"],
        "ex": ["Straight leg raise or Spurling test, dermatomal sensory loss",
               "Myotomal weakness and reflex loss localising the root",
               "Gait including heel and toe walking"],
    },

    # --- Musculoskeletal / rheumatological ----------------------------------
    "septic arthritis": {
        "hx": ["Rapid onset of a single hot swollen joint, unable to weight bear or move it",
               "Fever, recent injection or surgery, injecting drug use, prosthetic joint, immunosuppression"],
        "ex": ["Hot, swollen, exquisitely tender joint with near-complete loss of active and passive movement",
               "Fever and sepsis assessment; look for a portal of entry",
               "Aspiration before antibiotics wherever possible"],
    },
    "gout": {
        "hx": ["Rapid overnight onset, first metatarsophalangeal joint, exquisite pain, previous attacks",
               "Alcohol, diuretics, red meat, dehydration, renal impairment; tophi"],
        "ex": ["Hot, red, shiny, exquisitely tender joint, usually monoarticular",
               "Tophi at the ear, elbow and tendons; distinguishing it from sepsis needs aspiration"],
    },
    "rheumatoid": {
        "hx": ["Symmetrical small joint pain with morning stiffness over an hour, improving with use",
               "Duration over 6 weeks, functional impact, systemic features, family history"],
        "ex": ["Symmetrical MCP and PIP synovitis sparing DIPs; ulnar deviation, swan neck, boutonniere",
               "Squeeze test across MCPs and MTPs; function - grip, pinch, buttons",
               "Extra-articular: nodules, lung crackles, eyes, anaemia"],
    },
    "osteoarthritis": {
        "hx": ["Pain worse with use and at the end of the day, brief morning stiffness under 30 minutes",
               "Weight-bearing joints, previous injury, functional and sleep impact"],
        "ex": ["Bony swelling, crepitus, reduced range with a hard end-feel",
               "Heberden and Bouchard nodes; antalgic gait; muscle wasting"],
    },
    "polymyalgia": {
        "hx": ["Bilateral shoulder and hip girdle pain and stiffness over 45 minutes in the morning, age over 50",
               "Difficulty rising from a chair or combing hair; temporal arteritis symptoms",
               "Dramatic response to low-dose steroid if already started"],
        "ex": ["Restricted active shoulder and hip movement from pain, with preserved power once encouraged",
               "Temporal artery examination and visual acuity"],
    },
    "compartment syndrome": {
        "hx": ["Escalating pain out of proportion, unrelieved by opioids, after fracture, crush or reperfusion",
               "Paraesthesia and tightness; recent cast or tight dressing"],
        "ex": ["Pain on passive stretch of the compartment - the earliest and most reliable sign",
               "Tense, woody compartment; paraesthesia in the nerve crossing it",
               "Pulses are often preserved - their presence does not exclude it"],
    },
    "fracture": {
        "hx": ["Mechanism and energy of injury, ability to weight bear or use the limb immediately after",
               "Point of maximal pain, deformity, and any numbness or coldness distally",
               "Osteoporosis risk and whether the mechanism fits the injury"],
        "ex": ["Look, feel, move: deformity, swelling, bruising, point bony tenderness",
               "Neurovascular status distal to the injury, documented before and after any manipulation",
               "Examine the joint above and below and the overlying skin for an open injury"],
    },
    "osteomyelitis": {
        "hx": ["Deep bone pain over days to weeks, fever, diabetes, ulcer, prosthesis, injecting drug use"],
        "ex": ["Focal bony tenderness, overlying swelling and warmth, sinus or ulcer probing to bone",
               "Fever, and neurovascular assessment of the limb"],
    },
    "cellulitis": {
        "hx": ["Spreading erythema with pain and fever; portal of entry such as a bite, ulcer or tinea",
               "Diabetes, lymphoedema, venous insufficiency, immunosuppression; previous episodes"],
        "ex": ["Mark the erythema border with a pen and date it; assess warmth, tenderness and swelling",
               "Look for lymphangitis, regional lymphadenopathy and a portal of entry",
               "Exclude necrotising infection: pain out of proportion, crepitus, bullae, systemic toxicity"],
    },
    "necrotising": {
        "hx": ["Rapidly progressive pain out of proportion over hours, systemic toxicity, diabetes or recent surgery"],
        "ex": ["Pain out of proportion to appearance, tense oedema beyond the erythema, crepitus",
               "Skin bullae, dusky discolouration, anaesthesia over the area",
               "Haemodynamic instability - this is a surgical emergency"],
    },
    "back pain": {
        "hx": ["Red flags: age under 20 or over 50, trauma, night pain, weight loss, fever, cancer, steroids",
               "Neurological symptoms, bladder and bowel function, saddle sensation",
               "Yellow flags: work, mood, beliefs about the pain"],
        "ex": ["Inspection, spinal palpation and percussion tenderness, range of movement",
               "Straight leg raise, myotomes, dermatomes and reflexes in both legs",
               "Gait and perianal assessment if red flags are present"],
    },

    # --- Skin / trauma / burns ----------------------------------------------
    "burn": {
        "hx": ["Mechanism, agent, duration of contact, and whether it was in an enclosed space",
               "First aid given: cool running water for 20 minutes; tetanus status",
               "Voice change, cough or soot suggesting airway involvement"],
        "ex": ["Airway first: singed nasal hairs, soot, hoarseness, stridor",
               "Estimate total body surface area and depth; check for circumferential burns",
               "Peripheral perfusion, associated trauma, and analgesia adequacy"],
    },
    "head injury": {
        "hx": ["Mechanism, loss of consciousness, amnesia, vomiting, seizure",
               "Anticoagulants or antiplatelets, alcohol, and whether there was a fall from height",
               "Progression of headache and drowsiness since the event"],
        "ex": ["GCS with its components, pupils, focal neurology - repeated over time",
               "Scalp wounds, skull base signs: Battle sign, raccoon eyes, CSF leak, haemotympanum",
               "Cervical spine assessment and full trauma survey"],
    },
    "anaphylaxis": {
        "hx": ["Exposure to a known or new trigger and the interval to symptom onset",
               "Airway, breathing and circulatory symptoms; skin and gastrointestinal features",
               "Previous reactions, autoinjector use before arrival, asthma as a severity risk"],
        "ex": ["Airway: stridor, tongue and lip swelling, voice change - assess repeatedly",
               "Wheeze, work of breathing, saturations; blood pressure and perfusion",
               "Urticaria and angioedema; note the absence of skin signs does not exclude it"],
    },
    "urticaria": {
        "hx": ["Individual weals lasting under 24 hours, itch, triggers, drugs, foods, infection",
               "Angioedema, breathing or swallowing difficulty"],
        "ex": ["Blanching raised weals with normal overlying skin, dermographism",
               "Lips, tongue and airway for angioedema; observations for systemic involvement"],
    },
    "pressure": {
        "hx": ["Immobility, duration on a surface, nutrition, continence, sensation",
               "Pain, discharge, odour, and how long the area has been present"],
        "ex": ["Stage the ulcer, measure it, describe base, edges, exudate and surrounding skin",
               "Assess all pressure areas including heels and sacrum; probe for bone",
               "Nutritional and vascular status"],
    },
    "melanoma": {
        "hx": ["Change in a lesion: asymmetry, border, colour, diameter, evolution; bleeding or itch",
               "Sun exposure, burns, previous skin cancer, family history, skin type"],
        "ex": ["Full skin examination with dermoscopy; measure and photograph the lesion",
               "Regional lymph node basins and in-transit lesions"],
    },

    # --- ENT ----------------------------------------------------------------
    "epiglottitis": {
        "hx": ["Rapid onset over hours of sore throat out of proportion, drooling, muffled voice, fever",
               "Immunisation history and inability to swallow saliva"],
        "ex": ["Do not examine the throat or distress the patient - call anaesthetics and ENT",
               "Observe posture (tripod), drooling, stridor, work of breathing and saturations"],
    },
    "quinsy": {
        "hx": ["Unilateral severe sore throat, trismus, hot potato voice, referred ear pain, drooling"],
        "ex": ["Trismus, unilateral tonsillar swelling with uvular deviation",
               "Cervical lymphadenopathy, fever, and airway assessment"],
    },
    "tonsillitis": {
        "hx": ["Sore throat, fever, absence of cough, duration; ability to swallow fluids",
               "Recurrence frequency and previous antibiotic courses"],
        "ex": ["Tonsillar exudate and enlargement, anterior cervical lymphadenopathy, fever",
               "Trismus, uvular deviation or drooling would suggest a complication"],
    },
    "epistaxis": {
        "hx": ["Which side started, estimated volume, duration, anterior or posterior flow into the throat",
               "Anticoagulants, antiplatelets, hypertension, trauma, nose picking, bleeding disorder"],
        "ex": ["Haemodynamic state first, then anterior rhinoscopy for a Little area bleeding point",
               "Examine the oropharynx for posterior bleeding; assess clot and airway"],
    },
    "vertigo": {
        "hx": ["Timing and triggers: episodic with head movement, single prolonged episode, or recurrent spontaneous",
               "Duration of each attack, hearing loss, tinnitus, aural fullness",
               "Neurological symptoms and vascular risk suggesting a central cause"],
        "ex": ["Dix-Hallpike and head impulse, nystagmus characteristics, test of skew (HINTS)",
               "Cranial nerves, cerebellar signs, gait and Romberg",
               "Otoscopy and whisper or tuning fork hearing tests"],
    },
    "hearing loss": {
        "hx": ["Unilateral or bilateral, sudden or gradual, tinnitus, vertigo, ear discharge, pain",
               "Noise exposure, ototoxic drugs, trauma, family history"],
        "ex": ["Otoscopy of both ears, Rinne and Weber to separate conductive from sensorineural",
               "Cranial nerves, particularly the facial nerve; balance assessment"],
    },
    "otitis": {
        "hx": ["Ear pain, discharge, hearing change, fever, preceding upper respiratory infection",
               "Swimming, water exposure, hearing aid or cotton bud use"],
        "ex": ["Otoscopy: canal, drum colour, bulging, perforation, discharge",
               "Tragal tenderness for otitis externa; mastoid tenderness and pinna position for mastoiditis",
               "Facial nerve function and meningism"],
    },

    # --- Infection ----------------------------------------------------------
    "sepsis": {
        "hx": ["Time course of fever, rigors and functional decline; likely source by system",
               "Immunosuppression, recent surgery, lines, catheters, prostheses",
               "Travel, contacts, and antibiotics already taken"],
        "ex": ["Full observation set with respiratory rate and conscious level - calculate the score",
               "Perfusion, capillary refill, mottling, urine output",
               "Systematic source hunt: chest, abdomen, urine, skin, lines, joints, CNS"],
    },
    "infection": {
        "hx": ["Fever pattern, rigors, localising symptoms by system, and time course",
               "Travel, contacts, animal exposure, immunosuppression, recent procedures",
               "Antibiotics already taken and previous resistant organisms"],
        "ex": ["Full observations and a septic screen approach",
               "Systematic search for a source: chest, abdomen, urine, skin and soft tissue, lines, joints",
               "Rash, lymphadenopathy, new murmur"],
    },
    "abscess": {
        "hx": ["Localised swelling with increasing pain, fever, and any preceding wound or injection",
               "Diabetes and immunosuppression"],
        "ex": ["Fluctuant, tender, warm swelling with surrounding erythema; point of maximal fluctuance",
               "Regional lymphadenopathy, fever, and deep extension"],
    },
    "malaria": {
        "hx": ["Travel to an endemic area within the last year, with dates and prophylaxis adherence",
               "Fever pattern, rigors, headache, myalgia, jaundice, dark urine"],
        "ex": ["Temperature, conscious level, jaundice, pallor, splenomegaly",
               "Signs of severity: confusion, respiratory distress, oliguria, bleeding"],
    },
    "covid": {
        "hx": ["Fever, cough, anosmia, breathlessness, exertional desaturation; vaccination and contacts"],
        "ex": ["Saturations at rest and after exertion, respiratory rate, work of breathing",
               "Chest auscultation and signs of thromboembolism"],
    },
    "hiv": {
        "hx": ["Risk exposures, previous testing, seroconversion illness, weight loss, opportunistic infections",
               "Antiretroviral history and adherence"],
        "ex": ["Oral candida and hairy leukoplakia, generalised lymphadenopathy, skin lesions",
               "Weight, fundoscopy, chest and neurological examination"],
    },

    # --- Haematological -----------------------------------------------------
    "anaemia": {
        "hx": ["Fatigue, breathlessness on exertion, palpitations, dizziness and their time course",
               "Blood loss: menstrual, gastrointestinal, haematuria; diet and absorption",
               "Pica, restless legs, and family history of haemoglobinopathy"],
        "ex": ["Conjunctival and palmar crease pallor, tachycardia, flow murmur",
               "Koilonychia, angular stomatitis, glossitis for iron deficiency",
               "Jaundice and splenomegaly for haemolysis; rectal examination for melaena"],
    },
    "haemolysis": {
        "hx": ["Jaundice, dark urine, fatigue; drugs, infection, transfusion, family history"],
        "ex": ["Jaundice, pallor, splenomegaly",
               "Leg ulcers and gallstone-related right upper quadrant tenderness"],
    },
    "lymphoma": {
        "hx": ["Painless progressive lymphadenopathy, B symptoms: fever, drenching night sweats, weight loss",
               "Alcohol-induced node pain, itch, and duration of the nodes"],
        "ex": ["Palpate all node basins: cervical, supraclavicular, axillary, inguinal - size, consistency, fixity",
               "Hepatosplenomegaly, Waldeyer ring, skin infiltration",
               "Signs of compression: SVC obstruction, airway, cord"],
    },
    "leukaemia": {
        "hx": ["Fatigue, infections, bruising and bleeding over weeks; bone pain",
               "B symptoms and any prior chemotherapy or radiation"],
        "ex": ["Pallor, bruising, petechiae, gum hypertrophy, mouth ulcers",
               "Lymphadenopathy, hepatosplenomegaly, sternal tenderness",
               "Fever and a source of infection in a likely neutropenic patient"],
    },
    "myeloma": {
        "hx": ["Bone pain particularly in the back and ribs, fatigue, recurrent infection, weight loss",
               "Symptoms of hypercalcaemia and renal impairment"],
        "ex": ["Focal bony tenderness, pallor, hydration status",
               "Neurological examination for cord compression; signs of amyloid"],
    },
    "thrombocytopenia": {
        "hx": ["Bruising, petechiae, mucosal bleeding, menorrhagia; recent viral illness, drugs, heparin",
               "Alcohol, liver disease, and any recent transfusion"],
        "ex": ["Petechiae, purpura, wet purpura in the mouth, retinal haemorrhage on fundoscopy",
               "Splenomegaly, lymphadenopathy, signs of liver disease"],
    },
    "neutropenic": {
        "hx": ["Date of last chemotherapy - nadir is typically 7-14 days; any fever at home",
               "Localising symptoms, line site pain, mucositis, diarrhoea",
               "Prophylactic antibiotics and growth factor use"],
        "ex": ["Observations with a low threshold - antibiotics within one hour of recognition",
               "Examine mouth, perianal area, line sites, chest, skin - but avoid a rectal examination",
               "Perfusion and haemodynamic state"],
    },
    "sickle": {
        "hx": ["Comparison with the patient's usual crisis, sites of pain, precipitants such as cold or infection",
               "Chest pain and breathlessness suggesting acute chest syndrome; priapism; neurological symptoms",
               "Usual analgesic regimen and what works"],
        "ex": ["Sites of tenderness, temperature, saturations and respiratory examination",
               "Splenic size, jaundice, hydration, and neurological examination"],
    },

    # --- Oncological / palliative ------------------------------------------
    "malignancy": {
        "hx": ["Weight loss quantified, appetite, fatigue, night sweats and the time course",
               "Site-specific red flags: bleeding, dysphagia, cough, bowel or urinary change, lumps",
               "Smoking, alcohol, occupational exposure, family history, and prior cancer or screening"],
        "ex": ["Cachexia, pallor, and a full lymph node survey including supraclavicular nodes",
               "Abdominal masses and organomegaly, breast and testicular examination as relevant",
               "Bony tenderness, chest examination, and focal neurology for metastatic disease"],
    },
    "metastas": {
        "hx": ["Known primary and its stage; new bone pain, headache, seizures, jaundice or breathlessness",
               "Weight loss and functional decline"],
        "ex": ["Bony percussion tenderness particularly of the spine, and neurological examination",
               "Hepatomegaly, lymph nodes, chest signs and any effusion"],
    },
    "tumour": {
        "hx": ["Duration and growth rate of the lump or symptom, associated systemic features",
               "Risk factors and any prior malignancy"],
        "ex": ["Site, size, consistency, mobility, fixity to skin or deep tissue, overlying changes",
               "Draining lymph node basins and a general survey for spread"],
    },
    "svc obstruction": {
        "hx": ["Facial and arm swelling worse on bending forward or in the morning; headache, breathlessness",
               "Known thoracic malignancy or central line"],
        "ex": ["Facial and upper limb oedema, distended non-pulsatile neck and chest wall veins",
               "Pemberton sign, stridor, plethora, conscious level"],
    },

    # --- Obstetric / gynaecological ----------------------------------------
    "ectopic pregnancy": {
        "hx": ["Last menstrual period and pregnancy test; unilateral pain with or without bleeding",
               "Shoulder tip pain, dizziness, syncope; risk factors including PID, prior ectopic, IVF, coil"],
        "ex": ["Haemodynamic state including postural blood pressure",
               "Abdominal tenderness, guarding, peritonism; do not delay referral for a vaginal examination",
               "Pallor and signs of significant intra-abdominal bleeding"],
    },
    "pid": {
        "hx": ["Lower abdominal pain, deep dyspareunia, abnormal discharge, intermenstrual bleeding",
               "Sexual history including new partners and contraception; fever"],
        "ex": ["Bilateral lower abdominal tenderness, cervical motion tenderness, adnexal tenderness",
               "Fever, discharge on speculum, and pregnancy test in all cases"],
    },
    "ovarian": {
        "hx": ["Sudden severe unilateral pain with vomiting suggests torsion; bloating and early satiety over weeks suggests malignancy",
               "Menstrual history, pregnancy test, known cyst"],
        "ex": ["Unilateral adnexal tenderness or a palpable mass, peritonism",
               "Abdominal distension, ascites and lymph nodes if malignancy is suspected"],
    },

    # --- Psychiatric / functional / general --------------------------------
    "anxiety": {
        "hx": ["Circumstances, cognitions and avoidance; palpitations, paraesthesia, chest tightness",
               "Onset relative to any physical symptom, panic attack pattern, caffeine and stimulants",
               "Screen for depression and risk; substance use"],
        "ex": ["Full physical examination to exclude organic disease and to reassure credibly",
               "Observations at rest, thyroid examination, tremor"],
    },
    "depression": {
        "hx": ["Low mood and anhedonia most days for over two weeks; sleep, appetite, energy, concentration",
               "Risk assessment: thoughts of self-harm, plans, protective factors",
               "Alcohol, drugs, and organic contributors such as thyroid or anaemia"],
        "ex": ["Mental state examination: appearance, speech, mood, thought content, insight",
               "Physical examination for organic mimics including thyroid and neurological signs"],
    },
    "alcohol": {
        "hx": ["Quantify in standard drinks per week; CAGE or AUDIT-C; time of last drink",
               "Previous withdrawal, seizures or delirium tremens; dependence features"],
        "ex": ["Withdrawal signs: tremor, sweating, tachycardia, agitation, hallucinations",
               "Stigmata of chronic liver disease, nutritional state, Wernicke signs: ophthalmoplegia, ataxia, confusion"],
    },
    "medication": {
        "hx": ["A complete drug list including over-the-counter, herbal and recently stopped medicines",
               "Temporal relationship between starting or changing a drug and the symptom",
               "Adherence, doses, and any recent dose change or interaction"],
        "ex": ["Observations and system examination targeted to the suspected adverse effect",
               "Look for anticholinergic, serotonergic or extrapyramidal signs, and hydration"],
    },
    "drug": {
        "hx": ["Substances used, route, amount, time of last use, and co-ingestants",
               "Withdrawal history, injecting practice, and previous overdose"],
        "ex": ["Toxidrome recognition: pupils, skin, bowel sounds, temperature, conscious level",
               "Injection sites, signs of infection, and cardiorespiratory examination"],
    },
    "dehydration": {
        "hx": ["Intake and output, vomiting, diarrhoea, fever, diuretics and losses over how long"],
        "ex": ["Mucous membranes, skin turgor, capillary refill, postural blood pressure, JVP",
               "Weight change and urine output charting"],
    },
    "thyroid disease": {
        "hx": ["Weight, appetite, bowel habit, heat or cold intolerance, mood and menstrual change",
               "Neck swelling, eye symptoms, family history, amiodarone or lithium"],
        "ex": ["Inspect and palpate the thyroid from behind, ask the patient to swallow; auscultate for a bruit",
               "Pulse, tremor, reflexes, eye signs, skin and hair"],
    },
    "foreign body": {
        "hx": ["What, when and where; whether the object was seen entering; witnessed choking episode",
               "Ongoing symptoms: drooling, stridor, wheeze, pain on swallowing, voice change",
               "Button battery or magnet ingestion is a time-critical emergency"],
        "ex": ["Airway assessment first: stridor, voice, drooling, work of breathing",
               "Auscultate for unilateral wheeze or reduced air entry; inspect the entry site",
               "Do not attempt blind removal or provoke a partially obstructed airway"],
    },
    "trauma": {
        "hx": ["Mechanism and energy transfer, time since injury, and any loss of consciousness",
               "Anticoagulation, comorbidity, tetanus status; pain sites in order of severity"],
        "ex": ["Primary survey: airway with cervical spine control, breathing, circulation, disability, exposure",
               "Secondary head-to-toe survey with log roll and neurovascular assessment of every limb",
               "Repeat observations - trauma findings evolve"],
    },
    "haemorrhage": {
        "hx": ["Site, volume, duration and rate of bleeding; anticoagulants and antiplatelets",
               "Dizziness, syncope, breathlessness indicating significant loss"],
        "ex": ["Heart rate, blood pressure including postural drop, capillary refill, conscious level",
               "Identify and examine the bleeding site; look for concealed bleeding in chest, abdomen, pelvis, thighs"],
    },
}



# Second pass over the unmatched tail: entries added to raise keyword coverage.
DIFFERENTIAL_KB.update({
    "stone": {
        "hx": ["Colicky pain, haematuria, previous stones, fluid intake and occupation",
               "Fever or rigors, which would make this an infected obstructed system"],
        "ex": ["Renal angle tenderness with a soft abdomen; a restless patient unable to lie still",
               "Temperature, haemodynamic state, and palpation for an aortic aneurysm as a mimic"],
    },
    "cyst": {
        "hx": ["How long the swelling has been present, rate of growth, pain, discharge and previous episodes",
               "Any change suggesting rupture, torsion, infection or malignant transformation"],
        "ex": ["Site, size, consistency, fluctuance, transillumination, mobility and skin attachment",
               "Tenderness and overlying erythema suggesting infection; regional lymph nodes"],
    },
    "constipation": {
        "hx": ["Stool frequency and Bristol form, straining, incomplete emptying, and duration",
               "Fluid, fibre and mobility; opioids, anticholinergics, iron and calcium channel blockers",
               "Red flags: new onset over 50, weight loss, rectal bleeding, anaemia"],
        "ex": ["Abdominal distension, palpable faecal loading in the left colon, bowel sounds",
               "Digital rectal examination for loaded rectum, impaction, mass and anal tone"],
    },
    "ibd": {
        "hx": ["Chronic diarrhoea with blood or mucus, nocturnal symptoms, urgency and tenesmus",
               "Weight loss, mouth ulcers, eye and joint symptoms, perianal disease"],
        "ex": ["Abdominal tenderness or mass, perianal inspection, extraintestinal signs",
               "Nutritional state, anaemia, and evidence of toxic dilatation if acutely unwell"],
    },
    "stricture": {
        "hx": ["Progressive obstruction: dysphagia to solids then liquids, or reducing stool calibre",
               "Prior inflammation, surgery, radiation, caustic injury or instrumentation"],
        "ex": ["Nutritional state and weight; abdominal distension and high-pitched bowel sounds",
               "Lymph nodes and masses to identify a malignant cause"],
    },
    "neuropathy": {
        "hx": ["Distribution, symmetry and time course; burning, numbness or weakness predominant",
               "Diabetes, alcohol, B12, chemotherapy, renal disease and family history"],
        "ex": ["Map the sensory deficit and define its level; test reflexes and distal power",
               "Vibration, proprioception, monofilament, Romberg and gait; inspect the feet"],
    },
    "hyperkalaemia": {
        "hx": ["Renal impairment, ACE inhibitors, spironolactone, potassium supplements, NSAIDs",
               "Muscle weakness, palpitations; tissue breakdown from crush, burns or tumour lysis"],
        "ex": ["Pulse and rhythm; get an ECG immediately rather than relying on examination",
               "Volume status, urine output, and proximal muscle power"],
    },
    "reactive arthritis": {
        "hx": ["Recent gastrointestinal or genitourinary infection 1-4 weeks before joint symptoms",
               "Asymmetrical lower limb oligoarthritis; eye and urethral symptoms"],
        "ex": ["Asymmetrical large joint synovitis, enthesitis at the Achilles and plantar fascia",
               "Conjunctivitis, keratoderma blennorrhagica, circinate balanitis, dactylitis"],
    },
    "demyelination": {
        "hx": ["Previous episodes separated in time and site; optic neuritis and sensory symptoms",
               "Heat sensitivity, Lhermitte phenomenon, bladder symptoms and fatigue"],
        "ex": ["Visual acuity, colour vision, relative afferent pupillary defect, eye movements",
               "Upper motor neurone and cerebellar signs, sensory level, gait"],
    },
    "hypothermia": {
        "hx": ["Exposure, immersion, duration; alcohol, hypothyroidism, sepsis, immobility after a fall",
               "How long the patient was found down, and any preceding collapse"],
        "ex": ["Core temperature with a low-reading thermometer, conscious level, shivering or its absence",
               "Pulse, rhythm and perfusion; handle gently as the myocardium is irritable",
               "Look for the cause of the collapse and for pressure injury"],
    },
    "ild": {
        "hx": ["Insidious exertional breathlessness and dry cough over months",
               "Occupational, avian, mould and drug exposures; connective tissue disease symptoms"],
        "ex": ["Fine bibasal end-inspiratory crackles, clubbing, resting and exertional saturations",
               "Signs of connective tissue disease and pulmonary hypertension"],
    },
    "sleep apnoea": {
        "hx": ["Snoring, witnessed apnoeas, daytime somnolence with an Epworth score, morning headache",
               "Weight change, neck circumference, alcohol and sedatives; driving occupation"],
        "ex": ["Body mass index, neck circumference, crowded oropharynx and Mallampati score",
               "Signs of cor pulmonale and resting saturations"],
    },
    "obesity hypoventilation": {
        "hx": ["Daytime somnolence, morning headache, breathlessness; weight trajectory",
               "Snoring and witnessed apnoeas; sedatives and opioids"],
        "ex": ["Body mass index, resting saturations, respiratory rate, CO2 retention flap",
               "Signs of right heart failure: raised JVP, oedema"],
    },
    "musculoskeletal pain": {
        "hx": ["Reproducible with movement or position, localised, and related to a specific activity",
               "Absence of exertional, autonomic and pleuritic features"],
        "ex": ["Reproduce the pain by palpating the specific structure and by resisted movement",
               "Confirm normal cardiorespiratory examination before attributing the pain"],
    },
    "biliary": {
        "hx": ["Right upper quadrant pain after fatty food, radiating to the shoulder tip",
               "Jaundice, dark urine, pale stool, fever and previous gallstones"],
        "ex": ["Murphy sign, jaundice, right upper quadrant mass and tenderness",
               "Fever and haemodynamic state to identify cholangitis"],
    },
    "mitral stenosis": {
        "hx": ["Exertional breathlessness, haemoptysis, palpitations; rheumatic fever history",
               "Symptoms worsened by pregnancy, AF onset or infection"],
        "ex": ["Malar flush, tapping non-displaced apex, irregular pulse",
               "Loud first heart sound, opening snap and rumbling mid-diastolic murmur at the apex in left lateral position, bell, breath held in expiration"],
    },
    "aspiration": {
        "hx": ["Swallow difficulty, coughing on food or fluids, reduced conscious level or a witnessed event",
               "Stroke, dementia, alcohol, seizure, reflux and nasogastric feeding"],
        "ex": ["Bedside swallow screen before anything oral; voice quality and cough strength",
               "Right lower zone crackles or bronchial breathing; dentition and oral hygiene",
               "Conscious level and neurological examination"],
    },
    "obstruction": {
        "hx": ["Colicky pain, vomiting, distension and absolute constipation - and the order they appeared",
               "Previous surgery, hernia, malignancy and change in bowel habit"],
        "ex": ["Distension, tympanic percussion, high-pitched or absent bowel sounds",
               "Every hernial orifice and every scar; rectal examination",
               "Localised tenderness or peritonism suggesting strangulation"],
    },
    "volvulus": {
        "hx": ["Rapid gross distension with absolute constipation; chronic constipation, institutional care",
               "Previous similar episodes that resolved"],
        "ex": ["Gross tympanic distension, often asymmetrical, with an empty rectum",
               "Tenderness and peritonism indicating ischaemia"],
    },
    "hernia": {
        "hx": ["Lump reducibility, relation to straining, and any pain or vomiting suggesting obstruction",
               "Duration, previous repair, cough, constipation, heavy lifting"],
        "ex": ["Examine standing and lying, with and without cough impulse; assess reducibility",
               "Relation to the pubic tubercle to distinguish inguinal from femoral",
               "Tenderness, erythema and irreducibility indicating strangulation"],
    },
    "colorectal cancer": {
        "hx": ["Change in bowel habit over weeks, rectal bleeding, tenesmus, weight loss",
               "Iron deficiency anaemia, family history, previous polyps and screening history"],
        "ex": ["Abdominal mass, hepatomegaly, cachexia and pallor",
               "Digital rectal examination for a palpable low rectal tumour; supraclavicular nodes"],
    },
    "fournier": {
        "hx": ["Rapidly worsening perineal or scrotal pain, fever, diabetes or immunosuppression",
               "Recent perineal instrumentation, catheter or abscess"],
        "ex": ["Perineal and scrotal erythema, crepitus, necrosis, foul discharge, pain out of proportion",
               "Systemic toxicity and haemodynamic instability - urgent surgical referral"],
    },
    "uraemia": {
        "hx": ["Nausea, anorexia, itch, hiccups, confusion and reduced urine output",
               "Known renal disease, dialysis access and last dialysis session"],
        "ex": ["Asterixis, pericardial rub, uraemic fetor, scratch marks",
               "Volume status, blood pressure, conscious level and dialysis access"],
    },
    "rhabdomyolysis": {
        "hx": ["Long lie after a fall, crush, seizure, extreme exertion, statins or stimulants",
               "Muscle pain and weakness, dark tea-coloured urine"],
        "ex": ["Muscle tenderness and swelling; assess compartments for tenseness",
               "Volume status, urine colour and output, pressure areas"],
    },
    "interstitial nephritis": {
        "hx": ["New drug in the last days to weeks: antibiotics, PPIs, NSAIDs, allopurinol",
               "Rash, fever and arthralgia alongside a rising creatinine"],
        "ex": ["Rash, fever, and volume status; usually no specific renal findings",
               "Review the drug chart at the bedside as part of the examination"],
    },
    "shingles": {
        "hx": ["Burning or tingling pain preceding the rash by days, in a strip on one side only",
               "Immunosuppression, age, and any eye or ear involvement"],
        "ex": ["Grouped vesicles on an erythematous base in a single dermatome, not crossing the midline",
               "Nasociliary tip involvement (Hutchinson sign) and the ear for Ramsay Hunt",
               "Facial nerve function and corneal assessment where relevant"],
    },
    "motor neurone disease": {
        "hx": ["Painless progressive weakness, wasting, fasciculation, cramps; no sensory symptoms",
               "Bulbar symptoms: slurred speech, choking, drooling; breathlessness lying flat"],
        "ex": ["Mixed upper and lower motor neurone signs in the same limb without a sensory level",
               "Tongue wasting and fasciculation, brisk jaw jerk, wasted fasciculating limbs",
               "Forced vital capacity and cough strength"],
    },
    "angiodysplasia": {
        "hx": ["Painless intermittent dark or fresh rectal bleeding, or iron deficiency anaemia",
               "Age, aortic stenosis, renal disease, anticoagulants"],
        "ex": ["Signs of anaemia, haemodynamic state, rectal examination and stool inspection",
               "Cardiac auscultation for aortic stenosis"],
    },
    "food bolus": {
        "hx": ["Sudden inability to swallow during a meal, drooling, chest discomfort; what was eaten",
               "Prior dysphagia suggesting an underlying stricture or eosinophilic oesophagitis"],
        "ex": ["Airway assessment and ability to handle saliva",
               "Surgical emphysema in the neck would suggest perforation"],
    },
    "shock": {
        "hx": ["Fluid losses, bleeding, infection, cardiac symptoms, allergen exposure - work through the causes",
               "Speed of onset and response to any treatment already given"],
        "ex": ["Heart rate, blood pressure, capillary refill, mottling, conscious level, urine output",
               "JVP to separate hypovolaemic from cardiogenic and obstructive causes",
               "Warm versus cold peripheries; source hunt for sepsis and bleeding"],
    },
    "fever": {
        "hx": ["Duration, pattern, rigors, and localising symptoms taken system by system",
               "Travel with dates, contacts, animals, immunosuppression, lines and prostheses"],
        "ex": ["Full observations and a systematic source hunt across every system",
               "Rash, lymph nodes, new murmur, hepatosplenomegaly, line sites and joints"],
    },
    "pregnancy": {
        "hx": ["Last menstrual period and a pregnancy test in any woman of reproductive age",
               "Bleeding, pain, gestation, previous pregnancies and complications"],
        "ex": ["Haemodynamic state, abdominal tenderness and fundal height if applicable",
               "Defer intimate examination to the appropriate team when ectopic is possible"],
    },
    "granuloma": {
        "hx": ["Systemic features: fever, weight loss, cough, eye and skin involvement over months",
               "Exposures, travel, occupation and family history"],
        "ex": ["Skin lesions, lymphadenopathy, eye examination, chest auscultation",
               "Hepatosplenomegaly and parotid or lacrimal enlargement"],
    },
    "diuretic": {
        "hx": ["Which diuretic, dose and any recent change; weight and urine output response",
               "Dizziness on standing, cramps and confusion suggesting electrolyte disturbance"],
        "ex": ["Volume status, lying and standing blood pressure, weight chart",
               "Signs of the condition being treated: JVP, oedema, chest crackles"],
    },
    "diabetic kidney disease": {
        "hx": ["Duration of diabetes, glycaemic control, blood pressure, proteinuria and retinopathy",
               "ACE inhibitor or SGLT2 use and any recent change"],
        "ex": ["Blood pressure, oedema, fundoscopy for retinopathy as a marker of microvascular disease",
               "Foot examination and volume status"],
    },
    "papillary necrosis": {
        "hx": ["Haematuria and loin pain in a patient with diabetes, sickle cell or analgesic use",
               "Passage of tissue in the urine and preceding infection"],
        "ex": ["Renal angle tenderness, fever, volume status and urine inspection"],
    },
    "av fistula": {
        "hx": ["Dialysis history, fistula age, needling problems, bleeding, hand pain or weakness",
               "Reduced flow or missed dialysis sessions"],
        "ex": ["Inspect, palpate for thrill and auscultate for bruit along the whole fistula",
               "Aneurysmal change, overlying skin, and distal hand perfusion for steal syndrome"],
    },
    "fistula": {
        "hx": ["Discharge type and volume, preceding abscess, surgery, radiation or inflammatory bowel disease",
               "Pneumaturia, faecaluria or faecal discharge depending on the site"],
        "ex": ["Inspect the external opening, discharge and surrounding skin; palpate the track",
               "Perianal inspection and examination for an underlying cause"],
    },
    "bladder cancer": {
        "hx": ["Painless visible haematuria, smoking, occupational dye or rubber exposure",
               "Irritative urinary symptoms and weight loss"],
        "ex": ["Abdominal and bimanual examination for a mass, palpable bladder",
               "Signs of anaemia and lymphadenopathy"],
    },
    "breast cancer": {
        "hx": ["Lump duration and change, skin or nipple change, discharge, pain",
               "Family history, hormonal factors, previous biopsies and screening"],
        "ex": ["Inspect in four positions, then palpate all four quadrants, tail and nipple with a chaperone",
               "Skin dimpling, peau d orange, nipple inversion; axillary and supraclavicular nodes",
               "Chest, spine and liver for metastatic disease"],
    },
    "hypertension": {
        "hx": ["Duration, readings at home, adherence, and any secondary cause symptoms",
               "End-organ symptoms: chest pain, breathlessness, visual change, headache"],
        "ex": ["Blood pressure in both arms with the correct cuff, and lying and standing",
               "Fundoscopy for hypertensive retinopathy, radiofemoral delay, renal bruits",
               "Apex character, heart sounds and signs of heart failure"],
    },
    "obesity": {
        "hx": ["Weight trajectory, diet, activity, sleep, mood and medications that promote weight gain",
               "Comorbidity screening: diabetes, apnoea, joints, fertility, mood"],
        "ex": ["Body mass index and waist circumference, blood pressure with an appropriate cuff",
               "Acanthosis nigricans, joints, skin folds and signs of endocrine causes"],
    },
    "wound infection": {
        "hx": ["Time since surgery or injury, increasing pain, discharge, fever and wound breakdown",
               "Diabetes, smoking, steroids and nutritional state"],
        "ex": ["Wound inspection: erythema, warmth, discharge, dehiscence, probe depth",
               "Mark the erythema border, check regional nodes, temperature and systemic signs"],
    },
    "eczema": {
        "hx": ["Itch, chronicity, flexural distribution, atopy and family history, triggers and irritants",
               "Treatment used, potency and adherence; sleep disturbance"],
        "ex": ["Ill-defined erythematous scaly patches in flexures, excoriation, lichenification",
               "Signs of infection: weeping, crusting, punched-out lesions of eczema herpeticum"],
    },
    "psoriasis": {
        "hx": ["Well-demarcated scaly plaques, extensor distribution, nail and joint symptoms",
               "Family history, triggers such as infection, stress, lithium and beta blockers"],
        "ex": ["Well-demarcated salmon-pink plaques with silvery scale on extensors and scalp",
               "Nail pitting and onycholysis, Auspitz sign, and joint examination for arthritis"],
    },
    "syncope": {
        "hx": ["Before, during and after - with a witness account; prodrome, posture and trigger",
               "Injury, incontinence, tongue bite, and time to full recovery",
               "Exertional or supine onset, palpitations, and family history of sudden death"],
        "ex": ["Lying and standing blood pressure, pulse rhythm, murmurs particularly aortic stenosis",
               "Injuries sustained, neurological examination, and capillary glucose"],
    },
    "vitamin b12": {
        "hx": ["Diet, vegan status, metformin, PPIs, gastric surgery, autoimmune disease",
               "Paraesthesia, unsteadiness, memory or mood change, glossitis"],
        "ex": ["Pallor, lemon tint, glossitis, angular stomatitis",
               "Dorsal column signs: vibration and proprioception loss, Romberg, brisk knees with absent ankles"],
    },
    "coagulopathy": {
        "hx": ["Bleeding pattern and site, previous surgery and dental extractions, family history",
               "Anticoagulants, liver disease, and recent transfusion or sepsis"],
        "ex": ["Bruising, petechiae, mucosal bleeding, joint or muscle haematoma",
               "Signs of liver disease and haemodynamic state"],
    },
    "transfusion": {
        "hx": ["Timing of symptoms relative to the transfusion, product type and volume given",
               "Fever, rash, breathlessness, back or infusion-site pain, dark urine",
               "Previous reactions and whether the pack details were checked"],
        "ex": ["Stop the transfusion first, then observations, rash and airway assessment",
               "Volume overload versus TRALI: JVP, crackles, saturations; urine colour"],
    },
    "tumour lysis": {
        "hx": ["Recent chemotherapy for a bulky or highly proliferative tumour; urine output",
               "Nausea, cramps, palpitations, seizures and lethargy"],
        "ex": ["Volume status and urine output, cardiac rhythm, tetany signs",
               "ECG at the bedside for hyperkalaemia rather than relying on examination"],
    },
    "chronic kidney": {
        "hx": ["Known baseline function, cause, proteinuria, and dialysis planning",
               "Uraemic symptoms, itch, cramps, appetite; nephrotoxic drugs"],
        "ex": ["Blood pressure, volume status, oedema, dialysis access if present",
               "Anaemia, scratch marks, and signs of bone disease"],
    },
})


# ---------------------------------------------------------------------------
# Layer 2: per-system fallbacks
# ---------------------------------------------------------------------------

SYSTEM_KB = {
    "Cardiovascular and respiratory presentations": {
        "hx": ["Exertional tolerance now versus baseline, orthopnoea and nocturnal symptoms",
               "Chest pain character, radiation and relation to exertion or breathing",
               "Palpitations, syncope, cough, sputum and haemoptysis",
               "Cardiovascular risk factors, smoking pack-years and occupational exposure"],
        "ex": ["Respiratory rate, saturations, pulse, blood pressure in both arms, temperature",
               "JVP, apex beat, heart sounds and murmurs with the patient at 45 degrees",
               "Chest expansion, percussion, auscultation and vocal resonance front and back",
               "Peripheral oedema, calf assessment and peripheral pulses"],
        "focus": "cardiorespiratory",
    },
    "Gastrointestinal and hepatobiliary presentations": {
        "hx": ["Site, radiation and character of pain, and its relation to meals and defaecation",
               "Vomiting, bowel habit change, blood in stool or vomit, weight loss",
               "Alcohol, medications including NSAIDs, travel and infectious contacts"],
        "ex": ["General inspection for jaundice, cachexia and stigmata of liver disease",
               "Inspect, palpate all nine regions starting away from the pain, percuss and auscultate",
               "Organomegaly, masses, shifting dullness, hernial orifices",
               "Offer a rectal examination and inspect the stool"],
        "focus": "abdominal",
    },
    "Renal, urinary and male genital presentations": {
        "hx": ["Urinary storage and voiding symptoms, haematuria, and urine output trend",
               "Loin or suprapubic pain, fever and rigors",
               "Nephrotoxic drugs, stones, catheters and instrumentation"],
        "ex": ["Volume status, blood pressure, and peripheral oedema",
               "Renal angle tenderness, palpable kidneys, palpable bladder and bladder scan",
               "External genitalia and digital rectal examination where relevant"],
        "focus": "renal and genitourinary",
    },
    "Endocrine and general systemic presentations": {
        "hx": ["Weight, appetite, energy, temperature tolerance and sleep",
               "Thirst, polyuria, mood, skin and hair change, menstrual history",
               "Steroid exposure, family history of endocrine and autoimmune disease"],
        "ex": ["Observations including capillary glucose, plus lying and standing blood pressure",
               "Thyroid inspection and palpation, eye signs, tremor and reflexes",
               "Skin, hair, body habitus, proximal muscle power and hydration"],
        "focus": "endocrine and general",
    },
    "Musculoskeletal and rheumatological presentations": {
        "hx": ["Which joints, symmetry, pattern of onset and duration of morning stiffness",
               "Relation to activity and rest, swelling, and functional impact on daily tasks",
               "Systemic features, rash, eye and bowel symptoms, family history"],
        "ex": ["Look, feel, move, and assess function - compare with the other side",
               "Active then passive range, joint line tenderness, effusion and warmth",
               "Examine the joint above and below, plus gait and special tests",
               "Screen the other joints and the skin, nails and eyes"],
        "focus": "musculoskeletal",
    },
    "Neurological presentations": {
        "hx": ["Exact onset and time course - abrupt, stepwise or progressive",
               "Anatomical distribution of the deficit and whether symptoms are negative or positive",
               "Headache, visual change, speech, swallow, bladder and bowel involvement",
               "A collateral witness account and vascular risk factors"],
        "ex": ["Conscious level and capillary glucose, then higher function and speech",
               "Cranial nerves, then tone, power, reflexes, coordination and sensation in all four limbs",
               "Gait, Romberg, and fundoscopy",
               "Blood pressure, pulse rhythm and carotid auscultation"],
        "focus": "neurological",
    },
    "Skin, wounds and trauma presentations": {
        "hx": ["Onset, distribution and evolution of the lesion or wound, and itch or pain",
               "Mechanism of injury, contamination, tetanus status and time since injury",
               "New drugs, contacts, travel and previous skin disease"],
        "ex": ["Describe the lesion: site, size, shape, colour, border, surface and distribution",
               "Assess the wound for depth, contamination, foreign body and tissue viability",
               "Neurovascular status distal to any wound, and regional lymph nodes",
               "Mucous membranes, nails and scalp"],
        "focus": "dermatological",
    },
    "Ear, nose and throat presentations": {
        "hx": ["Laterality, duration, pain, discharge, hearing or voice change, and nasal obstruction",
               "Swallowing, breathing and any red flags such as weight loss or a neck lump",
               "Noise exposure, trauma, smoking and alcohol"],
        "ex": ["Assess the airway and voice before anything else",
               "Otoscopy of both ears, tuning fork tests, anterior rhinoscopy and oral cavity inspection",
               "Palpate the neck systematically for lymph nodes and masses",
               "Cranial nerves, particularly the facial nerve"],
        "focus": "ENT",
    },
    "Infection and fever presentations": {
        "hx": ["Fever pattern and duration, rigors, and functional decline",
               "Localising symptoms taken system by system",
               "Travel with dates, contacts, animals, immunosuppression, lines and prostheses",
               "Antibiotics already taken and known resistant organisms"],
        "ex": ["Full observation set with respiratory rate and conscious level; calculate the sepsis score",
               "Systematic source hunt: chest, abdomen, urine, skin and soft tissue, lines, joints, CNS",
               "Rash, lymphadenopathy, new murmur and hepatosplenomegaly",
               "Perfusion, capillary refill and urine output"],
        "focus": "infective",
    },
    "Haematological presentations": {
        "hx": ["Fatigue, breathlessness, bruising, bleeding and infections over what time course",
               "Blood loss sources, diet, and B symptoms of fever, night sweats and weight loss",
               "Family history, drugs, alcohol and prior chemotherapy"],
        "ex": ["Pallor of conjunctivae and palmar creases, jaundice, bruising and petechiae",
               "Full lymph node survey and examination for hepatosplenomegaly",
               "Mouth for ulcers and gum changes, and fundoscopy",
               "Observations and any focus of infection"],
        "focus": "haematological",
    },
    "Oncological emergencies and communication": {
        "hx": ["The known diagnosis, stage, current treatment and date of the last cycle",
               "New pain, neurological symptoms, breathlessness, confusion or bleeding",
               "Performance status, goals of care and any advance care directive",
               "What the patient already understands and what they want to know"],
        "ex": ["Observations with a low threshold for treating neutropenic sepsis",
               "Site-directed examination for cord compression, SVC obstruction and effusions",
               "Bony tenderness, neurological examination, hydration and mental state",
               "Lines, mouth and skin for a source of infection"],
        "focus": "oncological",
    },
}


# Generic clinical scaffolding used in every practice card.
OPENING = [
    "Introduce yourself, confirm identity, gain consent and set the agenda in one sentence.",
    "Open question, then let the patient speak uninterrupted for 30 seconds before narrowing down.",
]

CLOSING = [
    "Ideas, concerns and expectations, plus the impact on work, driving and daily life.",
    "Summarise back in two sentences, check for anything missed, and signpost the plan.",
]

BACKGROUND = [
    "Past medical and surgical history, and any previous identical episode.",
    "Full medication list with allergies and adherence; over-the-counter and herbal medicines.",
    "Family history relevant to this presentation; smoking, alcohol and recreational drugs.",
    "Social situation, function, occupation and who is at home.",
]

EXAM_OPENING = [
    "Wash hands, introduce, consent, expose and position appropriately, ask about pain.",
    "End-of-bed inspection: how unwell, work of breathing, posture, colour, attachments and drug charts.",
    "Full observation set including respiratory rate, and a capillary glucose where relevant.",
]

EXAM_CLOSING = [
    "State the completion: relevant bedside tests, other systems, and any intimate examination with a chaperone.",
    "Thank the patient, re-cover them, wash hands, then present a one-line summary with your leading diagnosis.",
]


# ---------------------------------------------------------------------------
# Patient roleplay layer
# ---------------------------------------------------------------------------
# The roleplay view is a simulated-patient brief, which is how real OSCE actor
# briefs work: instructions on what to disclose and when, not a verbatim script.
# Each doctor prompt is rendered into lay language and tagged with a disclosure
# rule, so two people can run the station from one screen.

# Disclosure rule per history block index.
DISCLOSURE = [
    "Volunteer freely",   # 01 open and orient
    "Only if asked",      # 02 focused discriminators - the discriminating detail
    "Only if asked",      # 03 background
    "Only if asked",      # 04 red flags and close
]

# Clinical term -> lay phrasing, applied longest-key-first.
LAY = {
    "shortness of breath": "being short of breath",
    "exertional breathlessness": "getting puffed out when you move around",
    "breathlessness": "being short of breath",
    "orthopnoea": "not being able to lie flat without getting breathless",
    "paroxysmal nocturnal dyspnoea": "waking in the night fighting for breath",
    "haemoptysis": "coughing up blood",
    "haematemesis": "vomiting blood",
    "melaena": "black, tarry, foul-smelling stools",
    "haematuria": "blood in your urine",
    "dysuria": "stinging or burning when you pass urine",
    "nocturia": "getting up at night to pass urine",
    "polyuria": "passing much more urine than usual",
    "polydipsia": "being much thirstier than usual",
    "dysphagia": "food or drink sticking on the way down",
    "odynophagia": "pain when you swallow",
    "syncope": "blacking out",
    "presyncope": "feeling like you were about to black out",
    "palpitations": "being aware of your heart racing or thumping",
    "claudication": "cramping pain in your legs when you walk",
    "paraesthesia": "pins and needles",
    "pruritus": "itching",
    "arthralgia": "aching joints",
    "myalgia": "aching muscles",
    "photophobia": "light hurting your eyes",
    "phonophobia": "noise bothering you",
    "rigors": "shaking chills you could not control",
    "pyrexia": "fever",
    "anorexia": "losing your appetite",
    "cachexia": "losing a lot of weight and muscle",
    "steatorrhoea": "pale, greasy stools that float and are hard to flush",
    "tenesmus": "feeling you still need to go after opening your bowels",
    "pneumaturia": "bubbles or air in your urine",
    "faecaluria": "urine that smells of stool",
    "hesitancy": "having to wait for the stream to start",
    "terminal dribble": "dribbling at the end of passing urine",
    "amaurosis fugax": "a curtain coming down over the vision in one eye",
    "diplopia": "double vision",
    "dysarthria": "slurred speech",
    "dysphasia": "trouble finding or understanding words",
    "ataxia": "being unsteady on your feet",
    "vertigo": "the room spinning around you",
    "tinnitus": "ringing in your ears",
    "otorrhoea": "discharge from your ear",
    "otalgia": "ear pain",
    "epistaxis": "nosebleeds",
    "trismus": "not being able to open your mouth wide",
    "dyspareunia": "pain during sex",
    "menorrhagia": "unusually heavy periods",
    "amenorrhoea": "your periods stopping",
    "oedema": "swelling",
    "erythema": "redness of the skin",
    "urticaria": "an itchy raised rash like nettle stings",
    "angioedema": "swelling of your lips, tongue or face",
    "jaundice": "your skin or eyes turning yellow",
    "asterixis": "your hands flapping when you hold them out",
    "confusion": "being muddled or not thinking straight",
    "seizure": "a fit",
    "aura": "an odd warning feeling beforehand",
    "post-ictal": "the drowsy, muddled period afterwards",
    "incontinence": "losing control of your bladder or bowels",
    "saddle anaesthesia": "numbness between your legs, where a saddle would touch",
    "atopy": "asthma, hay fever or eczema",
    "pack-years": "how much you have smoked over the years",
}
# Only concrete symptom nouns belong in LAY. Abstract clinical scaffolding
# ("onset", "trigger", "time course") reads as nonsense when substituted
# mid-sentence - "the interval to symptom how it started" - so it stays out.


# Presenting complaints in the patient's own words. Anything absent from this
# map is already lay enough to say out loud ("chest pain", "cough", "vomiting").
PRESENTATION_LAY = {
    "stridor": "noisy, harsh breathing",
    "dyspnoea": "trouble getting my breath",
    "haemoptysis": "coughing up blood",
    "pleuritic chest pain": "a sharp pain in my chest when I breathe in",
    "syncope": "blacking out",
    "palpitations": "my heart racing and thumping",
    "haematemesis and melaena": "vomiting blood and passing black, tarry stools",
    "dysphagia": "food sticking when I swallow",
    "jaundice": "going yellow",
    "anal pain and/or tenesmus": "pain at my back passage and feeling I still need to go",
    "oliguria / decreased urine output": "hardly passing any urine",
    "haematuria": "blood in my urine",
    "dysuria": "burning when I pass urine",
    "nocturia": "getting up all night to pass urine",
    "polyuria": "passing far more urine than usual",
    "urinary incontinence": "leaking urine",
    "faecal incontinence": "not making it to the toilet in time",
    "difficulty passing urine / urinary retention": "not being able to pass urine",
    "erectile dysfunction": "problems getting an erection",
    "malabsorption": "pale, greasy stools and losing weight",
    "hirsutism": "hair growing where I do not want it",
    "acute monoarthritis": "one joint suddenly hot, swollen and agonising",
    "polyarthritis, 5 or more joints": "lots of my joints aching and swelling",
    "oligoarthritis, 2 to 4 joints": "a few joints swollen and sore",
    "soft tissue rheumatism": "aching around my joints rather than in them",
    "fit and/or blackout": "a funny turn where I lost consciousness",
    "focal weakness and lesion localisation": "weakness down one side",
    "vertigo and dizziness": "the room spinning around me",
    "numbness and tingling": "numbness and pins and needles",
    "pruritus": "itching all over",
    "epistaxis": "nosebleeds",
    "hoarseness": "my voice going husky",
    "rhinorrhoea": "a constantly runny nose",
    "tinnitus": "ringing in my ears",
    "ear pain and/or discharge": "earache and discharge from my ear",
    "sore throat": "a very sore throat",
    "unintentional weight loss": "losing weight without trying",
    "excessive daytime sleepiness": "falling asleep during the day",
    "limb swelling": "my leg swelling up",
    "painful limb": "a very painful leg",
    "changing skin lesion, nodule, papule or ulcer": "a spot on my skin that has changed",
    "lymphadenopathy": "lumps in my neck",
    "abdominal distension": "my belly swelling up",
    "change in bowel habit": "my bowels not behaving as they used to",
    "recurrent infections": "one infection after another",
    "bleeding disorder": "bruising and bleeding far too easily",
    "sepsis": "feeling dreadful with a fever",
    "fever of unknown origin": "a fever that will not go away",
    "fever in the returned traveller": "a fever since I got back from my trip",
    "common bacterial infections": "an infection that is not settling",
    "multisystem disease, vasculitis or connective tissue disorder":
        "all sorts of things wrong at once - rashes, joints and feeling unwell",
    "raised intracranial pressure": "a headache that is worst when I wake up",
    "repeated falls": "falling over again and again",
    "skin failure": "my skin breaking down over large areas",
}

# Presentations that are a finding or a task rather than something a patient
# walks in complaining of. The actor is briefed as having been told the finding.
FINDING_PRESENTATIONS = {
    "lung nodule on chest x-ray", "perforated viscus", "acute kidney injury",
    "chronic kidney disease", "proteinuria", "renal mass", "scrotal mass",
    "abdominal mass", "pituitary mass", "adrenal mass", "neck mass",
    "solitary thyroid nodule", "space-occupying lesion in the brain",
    "brain death, neurological determination of death", "pancytopenia",
    "raised red cell or white cell count", "splenomegaly",
    "spinal cord compression", "superior vena cava obstruction",
    "acute malignancy-related hypercalcaemia", "breaking bad news",
    "febrile neutropenia / immunosuppressed patient with fever",
    "fever in the perioperative or hospital-acquired setting",
    "fracture, traumatic versus pathological", "heart murmur",
    "foreign body in gastrointestinal tract", "ear, nose or throat foreign body",
}

# Affective cue per system, so the actor has something to play.
AFFECT = {
    "Cardiovascular and respiratory presentations":
        "Play it breathless: short sentences, pause for air, sit forward if it helps.",
    "Gastrointestinal and hepatobiliary presentations":
        "Guard the sore area with your hand and be reluctant to let it be pressed.",
    "Renal, urinary and male genital presentations":
        "Be embarrassed about the urinary details and only give them once asked plainly.",
    "Endocrine and general systemic presentations":
        "Play it tired and flat, and mention how long you have felt not yourself.",
    "Musculoskeletal and rheumatological presentations":
        "Move stiffly, and wince when the affected part is moved rather than touched.",
    "Neurological presentations":
        "If the brief says confused, answer slightly off the question and let a relative correct you.",
    "Skin, wounds and trauma presentations":
        "Be worried about scarring and about whether it will need stitches or surgery.",
    "Ear, nose and throat presentations":
        "Speak quietly or hoarsely, and ask the doctor to repeat things if hearing is the issue.",
    "Infection and fever presentations":
        "Play it unwell and shivery, pulling the blanket up, with a poor sense of time.",
    "Haematological presentations":
        "Play it exhausted, and mention bruises you cannot account for only when asked.",
    "Oncological emergencies and communication":
        "Be frightened and looking for reassurance; ask directly whether this is the cancer spreading.",
}

CLOSING_PATIENT = [
    "If asked what you are worried about, give the concern in the brief - do not offer it unprompted.",
    "If the doctor summarises accurately, confirm it; if they miss something important, stay quiet.",
]
