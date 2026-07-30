"""Investigations and confirmatory tests for every pathology in the knowledge base.

Merged into DIFFERENTIAL_KB as the 'ix' field, which renders as the
"What confirms or grades it" block in the examination view. Kept in its own
module because it is a large, flat, independently-reviewable table.

Each entry lists the bedside and first-line tests that actually change what you
do, and the diagnostic threshold or finding where one exists. It is deliberately
not an exhaustive work-up.
"""

IX = {

    # ---------------- Cardiovascular ----------------
    "angina": [
        "Resting ECG (often normal between episodes), FBC for anaemia, HbA1c, lipids, thyroid function.",
        "CT coronary angiography as first-line anatomical testing; functional imaging if inconclusive.",
    ],
    "aortic dissection": [
        "CT angiography of the aorta is the definitive test - do not delay it for other investigations.",
        "ECG to exclude ST-elevation MI, chest X-ray for a widened mediastinum, and crossmatch.",
        "Blood pressure in both arms documented, and troponin and D-dimer only if they will not delay imaging.",
    ],
    "pericarditis": [
        "ECG: widespread saddle-shaped ST elevation with PR depression.",
        "Echocardiography for an effusion, plus troponin, CRP and inflammatory markers.",
    ],
    "tamponade": [
        "Urgent echocardiography: diastolic collapse of the right atrium and ventricle.",
        "ECG may show low-voltage complexes and electrical alternans; chest X-ray a globular heart.",
    ],
    "heart failure": [
        "NT-proBNP; a normal level makes heart failure very unlikely.",
        "Echocardiography for ejection fraction and valve disease; ECG and chest X-ray.",
        "Urea and electrolytes, FBC, thyroid function, iron studies, and daily weights.",
    ],
    "arrhythmia": [
        "12-lead ECG during symptoms; ambulatory or event monitoring if intermittent.",
        "Electrolytes including potassium, magnesium and calcium; thyroid function; troponin if ischaemic.",
    ],
    "atrial fibrillation": [
        "12-lead ECG confirms the diagnosis: irregularly irregular with absent P waves.",
        "Thyroid function, urea and electrolytes, FBC; echocardiography for structural disease.",
        "CHA2DS2-VASc for stroke risk and ORBIT or HAS-BLED for bleeding risk.",
    ],
    "aortic stenosis": [
        "Echocardiography grades severity by valve area and mean gradient.",
        "ECG for left ventricular hypertrophy; chest X-ray; FBC for associated anaemia.",
    ],
    "endocarditis": [
        "Three sets of blood cultures from separate sites before antibiotics.",
        "Transthoracic then transoesophageal echocardiography for vegetations.",
        "Apply the modified Duke criteria; CRP, FBC, urinalysis for haematuria.",
    ],
    "orthostatic hypotension": [
        "Lying and standing blood pressure at 1 and 3 minutes - a fall of 20 systolic or 10 diastolic.",
        "FBC, urea and electrolytes, glucose; medication review; ECG.",
    ],
    "vasovagal": [
        "ECG and lying and standing blood pressure; a normal examination and ECG support the diagnosis.",
        "Consider tilt-table testing only where the diagnosis is genuinely unclear.",
    ],
    "peripheral vascular": [
        "Ankle-brachial pressure index: under 0.9 confirms disease, under 0.4 indicates critical ischaemia.",
        "Duplex ultrasound, then CT or MR angiography for planning; HbA1c and lipids.",
    ],
    "acute limb ischaemia": [
        "A clinical diagnosis - urgent vascular referral, do not delay for imaging.",
        "Handheld Doppler of the distal pulses; CT angiography only if it will not delay revascularisation.",
        "ECG for atrial fibrillation as the embolic source; creatine kinase and potassium for reperfusion injury.",
    ],
    "dvt": [
        "Two-level Wells score; D-dimer if unlikely, proximal leg vein ultrasound if likely.",
        "A negative D-dimer with a low Wells score excludes it; FBC, renal function and clotting before anticoagulation.",
    ],
    "venous insufficiency": [
        "Venous duplex ultrasound for reflux; ankle-brachial index before any compression therapy.",
    ],
    "mitral stenosis": [
        "Echocardiography for valve area and gradient; ECG for atrial fibrillation and P mitrale.",
        "Chest X-ray for left atrial enlargement and pulmonary congestion.",
    ],
    "hypertension": [
        "Ambulatory or home blood pressure monitoring to confirm before treating.",
        "End-organ assessment: urine albumin-to-creatinine ratio, urea and electrolytes, HbA1c, lipids, ECG, fundoscopy.",
        "Screen for secondary causes in the young, the resistant, or where features suggest it.",
    ],
    "syncope": [
        "12-lead ECG in every case, and lying and standing blood pressure.",
        "FBC, glucose, urea and electrolytes; pregnancy test where relevant.",
        "Echocardiography and ambulatory monitoring if exertional, supine, or with an abnormal ECG.",
    ],
    "shock": [
        "Serial lactate and venous or arterial gas; FBC, urea and electrolytes, clotting, crossmatch.",
        "Blood cultures if septic; ECG and echocardiography if cardiogenic; focused ultrasound for the cause.",
        "Continuous monitoring with hourly urine output.",
    ],

    # ---------------- Respiratory ----------------
    "pneumonia": [
        "Chest X-ray for consolidation; CRP, FBC, urea and electrolytes.",
        "CURB-65 to grade severity and direct where the patient is treated.",
        "Blood and sputum cultures, and pneumococcal and legionella urinary antigens if severe.",
    ],
    "pleural effusion": [
        "Chest X-ray then thoracic ultrasound; ultrasound-guided diagnostic aspiration.",
        "Light criteria on pleural fluid protein and LDH to separate exudate from transudate.",
        "Pleural fluid pH, glucose, cytology, microscopy and culture.",
    ],
    "bronchiectasis": [
        "High-resolution CT chest is diagnostic: bronchial dilatation with a signet-ring sign.",
        "Sputum culture including mycobacteria, immunoglobulins, aspergillus serology, and spirometry.",
    ],
    "tb": [
        "Chest X-ray, and three sputum samples for acid-fast bacilli, culture and nucleic acid testing.",
        "Isolate the patient pending results; HIV test in all cases.",
        "Interferon-gamma release assay or tuberculin testing for latent infection, not active disease.",
    ],
    "lung cancer": [
        "Urgent chest X-ray, then staging CT of chest, abdomen and pelvis.",
        "PET-CT and biopsy by bronchoscopy, EBUS or CT guidance for tissue diagnosis.",
        "Sodium and calcium for paraneoplastic syndromes; lung function before treatment.",
    ],
    "interstitial lung": [
        "High-resolution CT chest, and spirometry showing a restrictive pattern with reduced transfer factor.",
        "Autoimmune screen and precipitins for an underlying cause; oxygen saturation on exertion.",
    ],
    "ild": [
        "High-resolution CT chest, restrictive spirometry with reduced transfer factor.",
        "Autoimmune screen, precipitins, and exertional oxygen saturation.",
    ],
    "pulmonary hypertension": [
        "Echocardiography estimates pulmonary artery pressure; right heart catheterisation confirms it.",
        "ECG for right heart strain; lung function, CT and ventilation-perfusion scanning for the cause.",
    ],
    "sleep apnoea": [
        "Epworth sleepiness score, then overnight oximetry or polysomnography for the apnoea-hypopnoea index.",
        "Thyroid function and body mass index; advise on driving pending assessment.",
    ],
    "obesity hypoventilation": [
        "ABG for daytime hypercapnia; overnight oximetry or sleep study.",
        "Bicarbonate as a marker of chronic retention; lung function and echocardiography.",
    ],
    "aspiration": [
        "Chest X-ray, typically right lower or middle zone changes; oxygen saturations.",
        "Bedside swallow assessment and formal speech and language therapy review before oral intake.",
    ],
    "covid": [
        "PCR or rapid antigen testing; chest X-ray and oxygen saturation at rest and on exertion.",
        "CRP, FBC, urea and electrolytes; consider CT pulmonary angiography given the thrombotic risk.",
    ],

    # ---------------- Gastrointestinal / hepatobiliary ----------------
    "appendicitis": [
        "Urine dipstick and pregnancy test in every woman of reproductive age.",
        "FBC, CRP; ultrasound first in children and women, CT in adults where the diagnosis is unclear.",
        "Alvarado or similar scoring to support, not replace, clinical assessment.",
    ],
    "cholecystitis": [
        "Ultrasound of the biliary tree: stones, wall thickening, pericholecystic fluid, sonographic Murphy.",
        "FBC, CRP, liver function and amylase to separate it from cholangitis and pancreatitis.",
    ],
    "cholangitis": [
        "Liver function showing an obstructive picture, blood cultures, FBC, CRP, lactate.",
        "Ultrasound for duct dilatation, then MRCP or urgent ERCP for drainage.",
    ],
    "pancreatitis": [
        "Serum lipase or amylase over three times the upper limit of normal.",
        "Ultrasound for gallstones, and calcium, triglycerides and liver function for the cause.",
        "Glasgow-Imrie or similar severity score at 48 hours; CT only if complications are suspected.",
    ],
    "perforation": [
        "Erect chest X-ray for free air under the diaphragm; CT abdomen is more sensitive.",
        "FBC, CRP, lactate, amylase, clotting, group and save; urgent surgical referral.",
    ],
    "bowel obstruction": [
        "Abdominal X-ray for dilated loops; CT abdomen and pelvis defines level, cause and any ischaemia.",
        "Urea and electrolytes for the losses, lactate for ischaemia, group and save.",
    ],
    "obstruction": [
        "Abdominal X-ray then CT abdomen and pelvis for the level, cause and any ischaemia.",
        "Urea and electrolytes, lactate and group and save.",
    ],
    "diverticulitis": [
        "CT abdomen and pelvis confirms and grades it, and identifies abscess or perforation.",
        "FBC, CRP; avoid colonoscopy in the acute phase.",
    ],
    "peptic ulcer": [
        "H. pylori testing by urea breath test or stool antigen, off PPI for two weeks.",
        "FBC for anaemia; upper GI endoscopy if alarm features or over 55 with new symptoms.",
    ],
    "gord": [
        "A clinical diagnosis - trial of acid suppression; no test needed without alarm features.",
        "Endoscopy if dysphagia, weight loss, anaemia, vomiting or new symptoms over 55.",
    ],
    "gastroenteritis": [
        "Usually clinical; stool culture and PCR if bloody, prolonged, recent travel or antibiotics.",
        "C. difficile toxin after antibiotics; urea and electrolytes for the losses.",
    ],
    "inflammatory bowel": [
        "Faecal calprotectin to separate it from irritable bowel syndrome.",
        "FBC, CRP, albumin, iron and B12; stool culture and C. difficile to exclude infection.",
        "Colonoscopy with biopsies for diagnosis; abdominal X-ray if toxic dilatation is suspected.",
    ],
    "ibd": [
        "Faecal calprotectin, FBC, CRP, albumin; stool culture to exclude infection.",
        "Colonoscopy with biopsies; abdominal X-ray if toxic dilatation is suspected.",
    ],
    "coeliac": [
        "Tissue transglutaminase IgA with total IgA, taken while still eating gluten.",
        "Duodenal biopsy to confirm; FBC, iron, B12, folate and bone density.",
    ],
    "irritable bowel": [
        "A positive clinical diagnosis by symptom criteria after excluding alternatives.",
        "FBC, CRP, coeliac serology and faecal calprotectin to exclude the mimics.",
    ],
    "variceal": [
        "Urgent upper GI endoscopy for diagnosis and banding.",
        "FBC, clotting, liver function, crossmatch; Glasgow-Blatchford and Rockall scores.",
    ],
    "cirrhosis": [
        "Liver function, albumin, clotting and platelets; ultrasound with elastography.",
        "Non-invasive fibrosis scoring; a liver screen for the cause; endoscopy for varices.",
        "Child-Pugh or MELD for severity; ascitic tap if ascites is present.",
    ],
    "hepatitis": [
        "Liver function with a hepatitic pattern; viral hepatitis serology; paracetamol level.",
        "Clotting and INR as the marker of synthetic function and severity; ultrasound of the liver.",
    ],
    "ascites": [
        "Diagnostic ascitic tap with cell count, albumin, culture and cytology.",
        "Serum-ascites albumin gradient over 11 g/L indicates portal hypertension.",
        "Neutrophils over 250 per mm3 confirms spontaneous bacterial peritonitis.",
    ],
    "mesenteric ischaemia": [
        "CT angiography of the mesenteric vessels is the definitive test.",
        "Lactate and venous gas for a metabolic acidosis; a normal lactate does not exclude it early.",
    ],
    "aaa": [
        "Bedside ultrasound for the aneurysm; CT angiography only if the patient is stable.",
        "Crossmatch and activate the major haemorrhage protocol; do not delay theatre for imaging.",
    ],
    "biliary": [
        "Ultrasound of the biliary tree; liver function and amylase.",
        "MRCP if duct stones are suspected with a normal ultrasound.",
    ],
    "constipation": [
        "Usually clinical; abdominal X-ray only if obstruction or impaction is suspected.",
        "Urea and electrolytes, calcium, thyroid function; colonoscopy if red flags or new onset over 50.",
    ],
    "stricture": [
        "Endoscopy with biopsy to exclude malignancy; contrast studies or CT to define the length.",
    ],
    "volvulus": [
        "Abdominal X-ray: coffee-bean sign in sigmoid volvulus; CT confirms and shows ischaemia.",
        "Lactate, urea and electrolytes; urgent surgical referral.",
    ],
    "hernia": [
        "Usually clinical; ultrasound or CT if the diagnosis is uncertain or complications are suspected.",
        "Lactate and urgent surgical referral if irreducible and tender.",
    ],
    "colorectal cancer": [
        "Faecal immunochemical test in the symptomatic pathway; FBC for iron deficiency anaemia.",
        "Colonoscopy with biopsy, then staging CT chest, abdomen and pelvis with MRI rectum.",
        "Carcinoembryonic antigen as a baseline before treatment.",
    ],
    "angiodysplasia": [
        "FBC and iron studies; upper and lower GI endoscopy, then capsule endoscopy if both are normal.",
        "CT angiography or red cell scanning if actively bleeding.",
    ],
    "food bolus": [
        "Usually clinical; avoid barium. Urgent endoscopy if unable to swallow saliva.",
        "Chest X-ray if perforation is suspected; look for an underlying stricture afterwards.",
    ],

    # ---------------- Renal / urological ----------------
    "uti": [
        "Urine dipstick and midstream culture before antibiotics; avoid dipstick alone over 65 or if catheterised.",
        "FBC, CRP, urea and electrolytes if systemically unwell; blood cultures if febrile.",
    ],
    "pyelonephritis": [
        "Urine culture and blood cultures before antibiotics; FBC, CRP, urea and electrolytes, lactate.",
        "Ultrasound to exclude obstruction, urgently if a stone or single kidney is suspected.",
    ],
    "renal colic": [
        "Non-contrast CT of kidneys, ureters and bladder within 24 hours is the definitive test.",
        "Urine dipstick for blood, urea and electrolytes, FBC, CRP, calcium and urate.",
        "An infected obstructed system needs immediate decompression, not analgesia alone.",
    ],
    "stone": [
        "Non-contrast CT of kidneys, ureters and bladder; urine dipstick and culture.",
        "Urea and electrolytes, calcium and urate; stone analysis if passed.",
    ],
    "acute kidney injury": [
        "Urea and electrolytes with a baseline for comparison; stage by creatinine rise and urine output.",
        "Urine dipstick - blood and protein suggest an intrinsic renal cause needing urgent nephrology input.",
        "Ultrasound within 24 hours to exclude obstruction; venous gas for potassium and acidosis.",
    ],
    "chronic kidney": [
        "eGFR and urine albumin-to-creatinine ratio, staged and confirmed over at least 3 months.",
        "Ultrasound of the renal tract; haemoglobin, calcium, phosphate, PTH and vitamin D.",
    ],
    "urinary retention": [
        "Bladder scan for the post-void residual volume confirms it.",
        "Urea and electrolytes for obstructive nephropathy, urine dipstick and culture.",
        "Urgent MRI if cauda equina is possible; PSA only after the acute episode.",
    ],
    "testicular torsion": [
        "A clinical diagnosis - immediate surgical exploration; do not delay for imaging.",
        "Doppler ultrasound only where it will not delay theatre and the diagnosis is genuinely in doubt.",
    ],
    "epididymo-orchitis": [
        "Urine dipstick and culture; first-void urine nucleic acid testing for chlamydia and gonorrhoea.",
        "Ultrasound if torsion cannot be excluded or an abscess is suspected.",
    ],
    "bph": [
        "International Prostate Symptom Score, urine dipstick, post-void residual bladder scan.",
        "PSA after counselling; urea and electrolytes; frequency-volume chart.",
    ],
    "prostate cancer": [
        "PSA with counselling, digital rectal examination, then multiparametric MRI before biopsy.",
        "Bone scan or PSMA PET for staging where the risk is intermediate or high.",
    ],
    "nephrotic": [
        "Urine protein-to-creatinine ratio, serum albumin and lipids; 24-hour protein if needed.",
        "Autoimmune and viral screen, myeloma screen; renal biopsy in most adults.",
    ],
    "glomerulonephritis": [
        "Urine dipstick and microscopy for red cell casts; urine protein-to-creatinine ratio.",
        "Complement, ANCA, anti-GBM, ANA, ASO titre and virology; urgent renal biopsy.",
    ],
    "uraemia": [
        "Urea and electrolytes, venous gas, calcium and phosphate.",
        "Urgent dialysis assessment for refractory hyperkalaemia, acidosis, fluid overload, pericarditis or encephalopathy.",
    ],
    "rhabdomyolysis": [
        "Creatine kinase, typically over five times normal; urine dipstick positive for blood without red cells.",
        "Potassium, calcium, phosphate, urea and electrolytes, and venous gas; monitor urine output closely.",
    ],
    "interstitial nephritis": [
        "Urine dipstick and microscopy for white cells and casts; eosinophils may be present.",
        "Stop the culprit drug; renal biopsy if the diagnosis is unclear or function does not recover.",
    ],
    "papillary necrosis": [
        "Urine microscopy for sloughed papillae; CT urography or ultrasound.",
        "Urea and electrolytes, FBC, and a sickle screen where relevant.",
    ],
    "diabetic kidney disease": [
        "Urine albumin-to-creatinine ratio annually, eGFR, HbA1c and blood pressure.",
        "Fundoscopy for retinopathy as the corroborating microvascular marker.",
    ],
    "av fistula": [
        "Clinical assessment of thrill and bruit; duplex ultrasound for flow and stenosis.",
        "Fistulogram if intervention is planned; urgent renal referral if it has stopped working.",
    ],
    "fistula": [
        "CT or MRI to define the track; contrast studies for enteric fistulae.",
        "Examination under anaesthesia for perianal disease; assess nutrition and fluid losses.",
    ],
    "bladder cancer": [
        "Urgent cystoscopy is the key test; CT urogram for the upper tracts.",
        "Urine cytology; FBC and renal function.",
    ],
    "fournier": [
        "A clinical diagnosis - immediate surgical debridement, do not delay for imaging.",
        "Blood cultures, lactate, FBC, CRP, glucose; LRINEC score supports but never excludes it.",
    ],
    "hyperkalaemia": [
        "Immediate 12-lead ECG: tented T waves, flattened P waves, broad QRS, sine wave.",
        "Venous or arterial gas for a rapid potassium, then a formal laboratory sample.",
        "Urea and electrolytes, calcium, glucose and creatine kinase; review the drug chart.",
    ],

    # ---------------- Endocrine / metabolic ----------------
    "diabetes": [
        "HbA1c 48 mmol/mol or above, or fasting glucose 7.0 or above, or random glucose 11.1 with symptoms.",
        "Capillary glucose and ketones at the bedside; urine albumin-to-creatinine ratio.",
        "Annual foot, eye and renal screening; lipids and blood pressure.",
    ],
    "hyperthyroid": [
        "TSH suppressed with raised free T4 or T3; TSH-receptor antibodies for Graves disease.",
        "ECG for atrial fibrillation; thyroid ultrasound or uptake scanning where the cause is unclear.",
    ],
    "hypothyroid": [
        "TSH raised with low free T4; thyroid peroxidase antibodies for autoimmune cause.",
        "FBC, lipids, sodium and creatine kinase.",
    ],
    "adrenal": [
        "Short Synacthen test; paired 9am cortisol and ACTH.",
        "Urea and electrolytes for hyponatraemia with hyperkalaemia; glucose.",
        "In suspected crisis give hydrocortisone immediately - do not wait for the result.",
    ],
    "cushing": [
        "Overnight dexamethasone suppression, late-night salivary cortisol, or 24-hour urinary free cortisol.",
        "Then ACTH to separate pituitary, ectopic and adrenal causes; glucose, potassium and bone density.",
    ],
    "hypercalcaemia": [
        "Corrected calcium with albumin, plus PTH - the single most useful discriminator.",
        "Urea and electrolytes, phosphate, magnesium, vitamin D, myeloma screen; ECG for a short QT.",
        "Imaging for malignancy if PTH is suppressed.",
    ],
    "hyponatraemia": [
        "Paired serum and urine osmolality with urine sodium, taken before any fluids.",
        "Assess volume status clinically first - it directs the whole work-up.",
        "Thyroid function, 9am cortisol, glucose and lipids; check the rate of correction.",
    ],
    "thyroid disease": [
        "TSH first, then free T4 and T3 as indicated; thyroid antibodies.",
        "Ultrasound and fine-needle aspiration for a nodule or goitre.",
    ],
    "obesity": [
        "Body mass index and waist circumference; HbA1c, lipids, liver function, blood pressure.",
        "Thyroid function and Epworth score where indicated.",
    ],
    "dehydration": [
        "Urea and electrolytes with a urea-to-creatinine ratio, and venous gas.",
        "Fluid balance and daily weights; urine output and postural blood pressure.",
    ],

    # ---------------- Neurological ----------------
    "tia": [
        "Urgent specialist assessment; brain imaging, carotid Doppler, ECG for atrial fibrillation.",
        "Glucose, FBC, lipids, HbA1c; prolonged cardiac monitoring where the cause is unclear.",
    ],
    "subarachnoid": [
        "Non-contrast CT head within 6 hours of onset is highly sensitive.",
        "If CT is negative and it is over 6 hours, lumbar puncture at 12 hours for xanthochromia.",
        "CT angiography to identify the aneurysm; clotting and blood pressure.",
    ],
    "meningitis": [
        "Blood cultures and empirical antibiotics first - do not delay treatment for the lumbar puncture.",
        "Lumbar puncture for cell count, protein, glucose paired with serum, culture and meningococcal PCR.",
        "CT head first only if reduced GCS, focal signs, seizures or immunocompromise.",
    ],
    "encephalitis": [
        "MRI brain, EEG, and lumbar puncture with viral PCR including herpes simplex.",
        "Start aciclovir empirically while awaiting results; autoimmune antibodies if suspected.",
    ],
    "migraine": [
        "A clinical diagnosis by criteria - no imaging needed with a normal examination and typical history.",
        "Image only for red flags: thunderclap onset, focal signs, papilloedema, new headache over 50.",
    ],
    "temporal arteritis": [
        "ESR and CRP urgently, then start high-dose steroid immediately - do not wait for biopsy.",
        "Temporal artery biopsy within 2 weeks, or temporal artery ultrasound for a halo sign.",
        "Same-day ophthalmology review if there is any visual symptom.",
    ],
    "raised intracranial pressure": [
        "Urgent CT head; fundoscopy for papilloedema.",
        "Lumbar puncture with opening pressure only once a mass lesion is excluded.",
    ],
    "guillain": [
        "Serial forced vital capacity at the bedside is the measurement that drives escalation.",
        "Lumbar puncture showing raised protein with a normal cell count; nerve conduction studies.",
        "ECG and cardiac monitoring for autonomic instability.",
    ],
    "multiple sclerosis": [
        "MRI brain and spinal cord with contrast for lesions disseminated in time and space.",
        "Lumbar puncture for oligoclonal bands; visual evoked potentials.",
    ],
    "demyelination": [
        "MRI brain and cord with contrast; lumbar puncture for oligoclonal bands.",
        "Visual evoked potentials where optic neuritis is suspected.",
    ],
    "parkinson": [
        "A clinical diagnosis - refer untreated to a specialist.",
        "MRI or DaTscan only where the picture is atypical; review the drug chart for neuroleptics.",
    ],
    "delirium": [
        "Bedside attention testing with 4AT or CAM; capillary glucose.",
        "Full septic screen: FBC, CRP, urea and electrolytes, calcium, urine culture, chest X-ray, cultures.",
        "Bladder scan, medication review, and CT head only if focal signs, head injury or no cause found.",
    ],
    "dementia": [
        "Cognitive assessment with a validated tool, and a collateral history.",
        "Reversible-cause screen: FBC, urea and electrolytes, calcium, thyroid function, B12, folate, glucose.",
        "Structural imaging with CT or MRI to exclude other pathology.",
    ],
    "cauda equina": [
        "Emergency whole-spine MRI - the only test that matters, and it must not be delayed.",
        "Post-void bladder scan documented; do not wait for it before referring.",
    ],
    "spinal cord compression": [
        "Whole-spine MRI within 24 hours, sooner if there is a neurological deficit.",
        "Give dexamethasone once malignant compression is suspected; calcium, FBC and myeloma screen.",
    ],
    "peripheral neuropathy": [
        "Glucose or HbA1c, B12 and folate, urea and electrolytes, liver function, TSH, ESR.",
        "Serum protein electrophoresis; nerve conduction studies to define the pattern.",
    ],
    "neuropathy": [
        "HbA1c, B12, folate, urea and electrolytes, liver function, TSH, ESR, protein electrophoresis.",
        "Nerve conduction studies to separate axonal from demyelinating patterns.",
    ],
    "radiculopathy": [
        "A clinical diagnosis; MRI only if red flags, a progressive deficit, or surgery is being considered.",
        "Document myotomes, dermatomes and reflexes at baseline so change can be detected.",
    ],
    "motor neurone disease": [
        "Electromyography and nerve conduction studies; MRI brain and cord to exclude mimics.",
        "Forced vital capacity and sniff nasal pressure to monitor respiratory function.",
    ],
    "vitamin b12": [
        "Serum B12 and folate; intrinsic factor antibodies; FBC and blood film for macrocytosis.",
        "Treat B12 before folate to avoid precipitating subacute combined degeneration.",
    ],

    # ---------------- Musculoskeletal / rheumatological ----------------
    "septic arthritis": [
        "Urgent joint aspiration for Gram stain, culture and crystals before antibiotics.",
        "Blood cultures, FBC, CRP, ESR; X-ray as a baseline.",
        "Aspiration is the definitive test - a normal CRP does not exclude it.",
    ],
    "gout": [
        "Joint aspiration showing negatively birefringent needle-shaped crystals confirms it.",
        "Serum urate, but it may be normal during an attack - recheck at 4 to 6 weeks.",
        "Urea and electrolytes and glucose; always exclude septic arthritis first.",
    ],
    "rheumatoid": [
        "Rheumatoid factor and anti-CCP antibodies, ESR and CRP.",
        "X-rays of hands and feet for erosions; ultrasound for synovitis.",
        "Baseline FBC, liver and renal function before disease-modifying therapy.",
    ],
    "osteoarthritis": [
        "A clinical diagnosis in a typical patient over 45 with activity-related pain and brief stiffness.",
        "X-ray only if the diagnosis is uncertain or surgery is contemplated.",
    ],
    "polymyalgia": [
        "ESR and CRP, usually markedly raised, before starting steroid.",
        "Baseline FBC, urea and electrolytes, glucose, bone profile and creatine kinase to exclude mimics.",
        "A dramatic response to low-dose steroid supports the diagnosis.",
    ],
    "reactive arthritis": [
        "Joint aspiration to exclude sepsis; ESR, CRP, and stool or genitourinary testing for the trigger.",
        "HLA-B27 where the picture is unclear; ophthalmology review if the eye is involved.",
    ],
    "compartment syndrome": [
        "A clinical diagnosis - urgent fasciotomy; do not delay for tests.",
        "Compartment pressure measurement where the patient is unconscious or the picture is unclear.",
        "Creatine kinase, potassium and renal function for rhabdomyolysis.",
    ],
    "fracture": [
        "X-ray in two orthogonal views, including the joint above and below.",
        "CT or MRI if the X-ray is normal but suspicion is high, as in scaphoid and hip fractures.",
        "Document neurovascular status before and after any manipulation.",
    ],
    "osteomyelitis": [
        "MRI is the most sensitive test; plain X-ray changes are late.",
        "Blood cultures and bone biopsy for organism and sensitivities; CRP and ESR to monitor.",
    ],
    "back pain": [
        "No imaging for uncomplicated mechanical pain.",
        "Urgent MRI for cauda equina, cord compression, infection or malignancy red flags.",
        "FBC, CRP, ESR and myeloma screen if infection or malignancy is suspected.",
    ],
    "musculoskeletal pain": [
        "Usually no test; the diagnosis rests on reproducing the pain and a normal cardiorespiratory examination.",
        "Investigate only to exclude the serious alternative the history raises.",
    ],

    # ---------------- Skin, wounds and trauma ----------------
    "cellulitis": [
        "A clinical diagnosis; mark and date the erythema border to track response.",
        "FBC, CRP, blood cultures if febrile; swab only if the skin is broken or discharging.",
        "Ultrasound if an abscess is suspected; glucose to screen for diabetes.",
    ],
    "necrotising": [
        "A surgical emergency - immediate exploration, do not delay for imaging.",
        "Blood cultures, lactate, FBC, CRP, creatine kinase, glucose and clotting.",
        "LRINEC score may support the diagnosis but a low score never excludes it.",
    ],
    "wound infection": [
        "Wound swab or tissue sample for culture; FBC, CRP, blood cultures if systemically unwell.",
        "Imaging if deep collection or osteomyelitis is suspected; glucose.",
    ],
    "burn": [
        "Estimate total body surface area and depth; use a fluid resuscitation formula from the time of injury.",
        "ABG with carboxyhaemoglobin if smoke inhalation; FBC, urea and electrolytes, creatine kinase, group and save.",
        "Early referral to burns for airway involvement, large area, or specialist sites.",
    ],
    "head injury": [
        "CT head within 1 hour for GCS under 13, focal deficit, seizure, skull fracture signs or repeated vomiting.",
        "CT within 8 hours if on anticoagulants or with lesser risk factors; clotting and platelets.",
        "Serial GCS and pupil observations; cervical spine imaging by the Canadian C-spine rule.",
    ],
    "trauma": [
        "Primary survey with adjuncts: chest and pelvic X-ray, FAST or eFAST scan.",
        "Venous gas with lactate, FBC, clotting, crossmatch; activate major haemorrhage protocol if needed.",
        "Trauma CT once stable enough; repeat the primary survey after any deterioration.",
    ],
    "haemorrhage": [
        "FBC, clotting, fibrinogen, crossmatch and serial lactate; activate the major haemorrhage protocol.",
        "Imaging directed at the site; reverse anticoagulation early.",
    ],
    "hypothermia": [
        "Core temperature with a low-reading thermometer, and continuous cardiac monitoring.",
        "ECG for J waves and arrhythmia; glucose, urea and electrolytes, thyroid function, creatine kinase.",
    ],
    "urticaria": [
        "A clinical diagnosis; no test needed for uncomplicated acute urticaria.",
        "Investigate for a cause only if chronic, or with systemic features; observe if any airway involvement.",
    ],
    "eczema": [
        "A clinical diagnosis; swab if infection is suspected.",
        "Consider patch testing for contact allergy in persistent or atypical disease.",
    ],
    "psoriasis": [
        "A clinical diagnosis; assess severity and joint involvement with a screening tool.",
        "Baseline FBC, liver and renal function before systemic therapy.",
    ],
    "shingles": [
        "A clinical diagnosis; vesicle fluid PCR if it is atypical or the patient is immunocompromised.",
        "Same-day ophthalmology if the eye is involved; consider HIV testing if young or recurrent.",
    ],
    "pressure": [
        "Stage, measure and photograph the ulcer; swab or biopsy only if infection is suspected.",
        "Probe to bone and image if osteomyelitis is possible; albumin and nutritional assessment.",
    ],
    "melanoma": [
        "Dermoscopy, then urgent excision biopsy with a narrow margin - never a shave or punch biopsy.",
        "Breslow thickness determines staging and further management; imaging if thick or node-positive.",
    ],

    # ---------------- Ear, nose and throat ----------------
    "epiglottitis": [
        "Do not examine the throat or attempt investigation before the airway is secured.",
        "Diagnosis is made on fibreoptic laryngoscopy by an airway-skilled clinician in theatre.",
        "Blood cultures and antibiotics once the airway is safe.",
    ],
    "quinsy": [
        "A clinical diagnosis; needle aspiration or incision is both diagnostic and therapeutic.",
        "FBC, CRP, Monospot for glandular fever; CT only if a deep neck abscess is suspected.",
    ],
    "tonsillitis": [
        "FeverPAIN or Centor score to guide antibiotics; throat swab is rarely needed.",
        "Monospot or EBV serology if prolonged; FBC before any antibiotic if glandular fever is likely.",
    ],
    "epistaxis": [
        "FBC, clotting and group and save if bleeding is heavy or the patient is anticoagulated.",
        "Anterior rhinoscopy to find the bleeding point; ENT review if posterior or uncontrolled.",
    ],
    "vertigo": [
        "Dix-Hallpike for BPPV, and HINTS examination in acute continuous vertigo.",
        "A central pattern on HINTS needs urgent MRI - CT is not sensitive for posterior fossa stroke.",
        "Audiometry if hearing is affected.",
    ],
    "hearing loss": [
        "Otoscopy with Rinne and Weber, then formal pure-tone audiometry.",
        "Sudden sensorineural loss is an emergency: same-day ENT referral and MRI to exclude a vestibular schwannoma.",
    ],
    "otitis": [
        "Otoscopy is the diagnosis; swab discharge if it is persistent or treatment fails.",
        "Urgent imaging and admission if mastoiditis, facial palsy or intracranial spread is suspected.",
    ],
    "foreign body": [
        "Airway assessment first; do not attempt blind removal.",
        "Chest and neck X-ray for radio-opaque objects; a button battery or magnet needs immediate removal.",
        "Endoscopy or bronchoscopy is both diagnostic and therapeutic.",
    ],

    # ---------------- Infection ----------------
    "infection": [
        "Blood cultures before antibiotics, FBC, CRP, urea and electrolytes, lactate.",
        "Source-directed samples: urine, sputum, wound swab, stool, CSF as indicated.",
        "Imaging directed at the suspected source.",
    ],
    "fever": [
        "FBC, CRP, urea and electrolytes, liver function, blood cultures, urine culture, chest X-ray.",
        "Travel screen including malaria films where relevant; HIV test.",
    ],
    "abscess": [
        "Ultrasound to confirm and localise the collection; CT for deep abscesses.",
        "Culture the pus at drainage - drainage is the definitive treatment.",
    ],
    "malaria": [
        "Three thick and thin blood films over consecutive days, or a rapid antigen test.",
        "A single negative film does not exclude it; FBC, glucose, lactate, renal and liver function.",
        "Species and parasitaemia determine whether this is severe malaria.",
    ],
    "hiv": [
        "Fourth-generation HIV antigen and antibody test, repeated after the window period.",
        "CD4 count and viral load once positive; screen for co-infection and opportunistic disease.",
    ],
    "granuloma": [
        "Chest X-ray and CT; serum ACE and calcium in suspected sarcoidosis.",
        "Tissue biopsy for histology and mycobacterial culture; exclude TB before immunosuppression.",
    ],

    # ---------------- Haematological ----------------
    "anaemia": [
        "FBC with mean cell volume, and a blood film - the MCV directs everything that follows.",
        "Microcytic: ferritin and iron studies. Macrocytic: B12, folate, thyroid, liver function.",
        "Coeliac serology and endoscopy or colonoscopy for unexplained iron deficiency.",
    ],
    "haemolysis": [
        "Reticulocytes, bilirubin, LDH and haptoglobin; blood film for the mechanism.",
        "Direct antiglobulin test to separate immune from non-immune causes; G6PD where relevant.",
    ],
    "lymphoma": [
        "Excision lymph node biopsy - fine-needle aspiration is not adequate.",
        "FBC, LDH, urate, liver and renal function, HIV and hepatitis serology.",
        "CT or PET-CT for staging; bone marrow biopsy where indicated.",
    ],
    "leukaemia": [
        "Urgent FBC and blood film; immediate haematology referral if blasts are present.",
        "Clotting, LDH, urate, calcium, phosphate and renal function for tumour lysis.",
        "Bone marrow aspirate and trephine with immunophenotyping and cytogenetics.",
    ],
    "myeloma": [
        "Serum protein electrophoresis with immunofixation, serum free light chains, urine Bence Jones protein.",
        "FBC, calcium, renal function; whole-body MRI or CT for lytic lesions.",
        "Bone marrow biopsy for plasma cell percentage.",
    ],
    "thrombocytopenia": [
        "Repeat FBC in citrate to exclude platelet clumping, and a blood film.",
        "Clotting, liver function, HIV and hepatitis serology, B12 and folate.",
        "Urgent haematology input if there is bleeding, fever or a microangiopathic film.",
    ],
    "neutropenic": [
        "Blood cultures from peripheral and line sites, FBC, CRP, urea and electrolytes, lactate.",
        "Antibiotics within one hour of recognition - never wait for the neutrophil count.",
        "Chest X-ray, urine culture and site-directed samples; avoid rectal examination.",
    ],
    "sickle": [
        "FBC and reticulocytes compared with the patient's own baseline; group and save.",
        "Chest X-ray and ABG if acute chest syndrome is suspected; cultures if febrile.",
        "Transcranial Doppler or urgent imaging for neurological symptoms.",
    ],
    "coagulopathy": [
        "FBC, PT, APTT, fibrinogen and a blood film; mixing studies if a prolonged time is unexplained.",
        "Liver function and a drug history; factor assays and von Willebrand screen where indicated.",
    ],
    "transfusion": [
        "Stop the transfusion and recheck the patient and pack identity first.",
        "Return the unit to the laboratory; FBC, direct antiglobulin test, repeat crossmatch, cultures.",
        "Chest X-ray to separate overload from TRALI; urinalysis for haemoglobinuria.",
    ],
    "tumour lysis": [
        "Potassium, phosphate, calcium, urate, urea and creatinine, LDH - checked frequently.",
        "ECG and continuous cardiac monitoring for hyperkalaemia; strict fluid balance.",
    ],

    # ---------------- Oncological ----------------
    "malignancy": [
        "Direct investigation at the suspected primary and refer on the appropriate urgent pathway.",
        "FBC, urea and electrolytes, liver function, calcium, LDH; imaging guided by the site.",
        "Tissue diagnosis by biopsy before treatment wherever possible.",
    ],
    "metastas": [
        "Staging CT of chest, abdomen and pelvis; bone scan or MRI for skeletal disease.",
        "Calcium, liver function and LDH; biopsy of an accessible site if the primary is unknown.",
    ],
    "tumour": [
        "Imaging appropriate to the site, then tissue biopsy for histology.",
        "Staging investigations and baseline bloods before treatment.",
    ],
    "svc obstruction": [
        "Urgent CT with contrast of the thorax to confirm and identify the cause.",
        "Tissue diagnosis before treatment where the patient is stable enough; discuss stenting.",
    ],
    "breast cancer": [
        "Triple assessment: clinical examination, imaging with mammography or ultrasound, and core biopsy.",
        "Axillary ultrasound with biopsy of suspicious nodes; staging if locally advanced.",
    ],

    # ---------------- Obstetric / gynaecological ----------------
    "ectopic pregnancy": [
        "Urine or serum beta-hCG in every woman of reproductive age with abdominal pain.",
        "Transvaginal ultrasound; a pregnancy of unknown location needs serial hCG.",
        "FBC, group and save, crossmatch if unstable - do not delay theatre for imaging.",
    ],
    "pid": [
        "Pregnancy test, endocervical and vulvovaginal swabs for chlamydia and gonorrhoea.",
        "FBC, CRP; pelvic ultrasound if a tubo-ovarian abscess is suspected.",
        "Treat empirically on clinical suspicion rather than waiting for swab results.",
    ],
    "ovarian": [
        "Pregnancy test and pelvic ultrasound; urgent if torsion is suspected.",
        "CA125 with the risk of malignancy index in postmenopausal women; CT for staging.",
    ],
    "pregnancy": [
        "Urine or serum beta-hCG; ultrasound to confirm site and viability.",
        "FBC, blood group and antibody screen; consider anti-D where indicated.",
    ],

    # ---------------- Psychiatric / drugs / general ----------------
    "anxiety": [
        "Investigate to exclude organic mimics: thyroid function, FBC, glucose, ECG.",
        "Use a validated severity tool such as GAD-7; screen for depression and substance use.",
    ],
    "depression": [
        "PHQ-9 or equivalent, with a documented risk assessment.",
        "Exclude organic contributors: thyroid function, FBC, B12, folate, calcium, glucose.",
    ],
    "alcohol": [
        "AUDIT-C or CAGE; FBC for macrocytosis, liver function with a raised GGT, clotting.",
        "Glucose, magnesium, phosphate and thiamine status; use CIWA to score withdrawal.",
    ],
    "medication": [
        "Review the full drug chart against the timeline of symptoms - this is the key investigation.",
        "Drug levels where available; renal and liver function; ECG for QT prolongation.",
    ],
    "drug": [
        "Bedside glucose, ECG for QT and QRS, venous gas, paracetamol and salicylate levels.",
        "Urine drug screen rarely changes acute management; discuss with the poisons service.",
    ],
    "diuretic": [
        "Urea and electrolytes including magnesium, daily weights and fluid balance.",
        "Lying and standing blood pressure; review the dose against the response.",
    ],
    "cyst": [
        "Ultrasound to confirm it is cystic and define its characteristics.",
        "Aspiration or excision for diagnosis if complex, growing or symptomatic.",
    ],
}
