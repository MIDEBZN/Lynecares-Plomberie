export interface LpProblemItem {
  icon: string;
  title: string;
  description: string;
  urgencyHint?: string;
}

export interface LpSolutionItem {
  icon: string;
  title: string;
  description: string;
  equipment?: string;
}

export interface LpProcessStep {
  step: number;
  title: string;
  description: string;
  highlight?: string;
}

export interface LpPricingItem {
  title: string;
  amount: string;
  details: string;
  badge?: string;
}

export interface LpTestimonial {
  author: string;
  location: string;
  quote: string;
  service: string;
  context: string;
}

export interface LpFaqItem {
  question: string;
  answer: string;
}

export interface LpConfig {
  slug: string;
  serviceCategory: 'urgence' | 'debouchage' | 'fuite_depannage';
  metaTitle: string;
  metaDescription: string;
  canonicalPath: string;
  heroBadge: string;
  heroH1: string;
  heroSubheadline: string;
  heroPrimaryCtaText: string;
  heroReassurance: string;
  persistentBarCtaText: string;
  phoneNumberDisplay: string;
  phoneNumberTel: string;
  whatsappUrl: string;
  
  reassuranceStrip: Array<{ icon: string; title: string; subtitle: string }>;
  problemsSectionTitle: string;
  problemsSectionIntro: string;
  problems: LpProblemItem[];
  
  solutionsSectionTitle: string;
  solutionsSectionIntro: string;
  solutions: LpSolutionItem[];
  
  processSectionTitle: string;
  processSectionIntro: string;
  processSteps: LpProcessStep[];
  
  pricingSectionTitle: string;
  pricingSectionIntro: string;
  pricingItems: LpPricingItem[];
  pricingNotes: string[];
  
  testimonialsSectionTitle: string;
  testimonials: LpTestimonial[];
  
  coverageSectionTitle: string;
  coverageIntro: string;
  coverageTowns: Array<{ name: string; zip: string }>;
  coverageDisclaimer: string;
  
  formSectionTitle: string;
  formSectionIntro: string;
  formProblemOptions: Array<{ value: string; label: string }>;
  
  faqsSectionTitle: string;
  faqs: LpFaqItem[];
  
  finalCtaTitle: string;
  finalCtaSubtext: string;
  finalCtaButtonText: string;
}

export const LP_COMMON = {
  phoneDisplay: '0466 26 58 95',
  phoneTel: 'tel:+32466265895',
  whatsappBase: 'https://wa.me/32466265895',
  address: '188 Rue de Bois-de-Breux, 4020 Liège',
  companyName: 'Lynecares Plomberie Liégeoise',
  serviceArea: 'Liège et communes limitrophes',
  coverageTowns: [
    { name: 'Liège (Centre, Guillemins, Outremeuse)', zip: '4000 / 4020' },
    { name: 'Seraing (Jemeppe, Ougrée, Boncelles)', zip: '4100' },
    { name: 'Herstal', zip: '4040' },
    { name: 'Ans', zip: '4430' },
    { name: 'Saint-Nicolas / Montegnée', zip: '4420' },
    { name: 'Grâce-Hollogne', zip: '4460' },
    { name: 'Flémalle', zip: '4400' },
    { name: 'Oupeye', zip: '4680' },
    { name: 'Chaudfontaine / Vaux-sous-Chèvremont', zip: '4050' },
    { name: 'Beyne-Heusay / Grivegnée', zip: '4610 / 4030' },
    { name: 'Awans', zip: '4340' }
  ],
  coverageDisclaimer: 'Délai d’arrivée confirmé au téléphone selon votre localisation exacte et la disponibilité des techniciens d’astreinte.'
};

export const LP_SERVICES: Record<string, LpConfig> = {
  'urgence-plomberie-liege': {
    slug: 'urgence-plomberie-liege',
    serviceCategory: 'urgence',
    metaTitle: 'Plombier Urgence Liège | Dépannage Rapide & Devis Clair',
    metaDescription: 'Dépannage plomberie d’urgence à Liège : fuite d’eau active, tuyau cassé, WC débordant. Appel direct 0466 26 58 95, tarif communiqué au téléphone et devis avant travaux.',
    canonicalPath: '/lp/urgence-plomberie-liege/',
    heroBadge: 'Liège & 1ère couronne • Permanence téléphonique',
    heroH1: 'Plombier urgence à Liège',
    heroSubheadline: 'Fuite importante, tuyau cassé ou WC qui déborde. Appelez pour organiser votre dépannage rapide.',
    heroPrimaryCtaText: 'Appeler le 0466 26 58 95',
    heroReassurance: 'Tarif de déplacement communiqué au téléphone et devis présenté avant travaux.',
    persistentBarCtaText: 'Urgence : 0466 26 58 95',
    phoneNumberDisplay: LP_COMMON.phoneDisplay,
    phoneNumberTel: LP_COMMON.phoneTel,
    whatsappUrl: `${LP_COMMON.whatsappBase}?text=Bonjour%20Lynecares,%20j%27ai%20une%20urgence%20plomberie%20%C3%A0%20Li%C3%A8ge%20:`,
    
    reassuranceStrip: [
      { icon: '📋', title: 'Devis avant travaux', subtitle: 'Aucun frais engagé sans votre accord préalable' },
      { icon: '⏱️', title: 'Délai confirmé d’emblée', subtitle: 'Estimation réaliste selon votre commune' },
      { icon: '🛡️', title: 'Artisans qualifiés', subtitle: 'Techniciens équipés pour sécuriser les lieux' }
    ],
    
    problemsSectionTitle: 'Sinistres et urgences pris en charge sans délai',
    problemsSectionIntro: 'Lorsque l’eau menace votre logement ou votre commerce, chaque minute compte. Nous intervenons sur les pannes critiques pour limiter les dégâts.',
    problems: [
      {
        icon: '🌊',
        title: 'Fuite d’eau active & inondation',
        description: 'Rupture soudaine de tuyauterie, vanne d’arrêt bloquée ou percée. Nous vous guidons par téléphone pour fermer l’arrivée générale avant notre arrivée.',
        urgencyHint: 'Conseil immédiat par téléphone'
      },
      {
        icon: '💥',
        title: 'Tuyau percé ou canalisation éclatée',
        description: 'Canalisation en cuivre, plomb ou Alpex fendue par l’usure, un coup de bélier ou le gel. Sécurisation immédiate et remplacement du tronçon.',
        urgencyHint: 'Intervention sur place'
      },
      {
        icon: '🚽',
        title: 'WC bouché avec risque de débordement',
        description: 'Refoulement complet empêchant l’usage des sanitaires. Dégagement d’urgence au matériel professionnel adapté pour rétablir l’évacuation.',
        urgencyHint: 'Dépannage sanitaire prioritaire'
      },
      {
        icon: '🛑',
        title: 'Refoulement d’eaux usées',
        description: 'Colonne d’immeuble ou égout qui refoule dans la cave ou au rez-de-chaussée. Arrêt du refoulement et désobstruction de sécurité.',
        urgencyHint: 'Sécurisation sanitaire'
      },
      {
        icon: '⚡',
        title: 'Panne d’eau chaude critique',
        description: 'Boiler ou chauffe-eau électrique en surpression, groupe de sécurité qui fuit abondamment ou court-circuit sur l’installation.',
        urgencyHint: 'Mise en sécurité'
      }
    ],
    
    solutionsSectionTitle: 'Prestations d’urgence assurées sur Liège',
    solutionsSectionIntro: 'Nos véhicules d’intervention disposent du matériel nécessaire pour réparer ou colmater immédiatement la plupart des sinistres sanitaires.',
    solutions: [
      {
        icon: '🔧',
        title: 'Colmatage et remplacement express',
        description: 'Remplacement de vannes défectueuses, manchons de réparation, raccords à sertir ou soudure cuivre pour stopper net la perte d’eau.',
        equipment: 'Raccords agréés & matériel de plomberie pro'
      },
      {
        icon: '🌀',
        title: 'Désobstruction sanitaire urgente',
        description: 'Utilisation d’un furet mécanique motorisé pour débloquer les WC ou colonnes sans détériorer vos sanitaires ni les joints.',
        equipment: 'Furet mécanique professionnel'
      },
      {
        icon: '🛡️',
        title: 'Mise en sécurité électrique et hydraulique',
        description: 'Isolement des circuits d’eau sinistrés pour rétablir l’alimentation partielle du reste de votre maison si possible.',
        equipment: 'Vannes d’arrêt & sectionnement'
      },
      {
        icon: '📝',
        title: 'Attestation pour votre assurance',
        description: 'En cas de dégât des eaux, nous vous remettons une facture détaillée mentionnant l’origine de la panne pour votre déclaration de sinistre.',
        equipment: 'Rapport d’intervention clair'
      }
    ],
    
    processSectionTitle: 'Comment se passe votre appel d’urgence ?',
    processSectionIntro: 'Une méthode transparente en 3 étapes pour agir vite sans mauvaise surprise financière.',
    processSteps: [
      {
        step: 1,
        title: '1. Évaluation téléphonique & consignes',
        description: 'Vous décrivez le problème au 0466 26 58 95. Nous vous indiquons les gestes réflexes (couper la vanne d’arrêt) et confirmons notre disponibilité.',
        highlight: 'Consignes de sécurité directes'
      },
      {
        step: 2,
        title: '2. Confirmation du tarif et du délai',
        description: 'Avant tout déplacement, nous vous annonçons les frais de déplacement et le taux horaire applicables selon l’horaire (journée ou astreinte).',
        highlight: 'Tarif clair dès l’appel'
      },
      {
        step: 3,
        title: '3. Diagnostic sur place, devis & réparation',
        description: 'Le technicien examine le sinistre, établit un devis ferme pour la réparation. Les travaux ne commencent qu’après votre accord exprès.',
        highlight: 'Devis signé avant travaux'
      }
    ],
    
    pricingSectionTitle: 'Tarification claire & conditions transparentes',
    pricingSectionIntro: 'Pas de devis flou ni de facturation abusive. Nos tarifs de référence sont annoncés avant tout déplacement :',
    pricingItems: [
      {
        title: 'Frais de déplacement',
        amount: '45 €',
        details: 'Applicable sur Liège et sa première couronne. Facturé uniquement lors d’un déplacement effectif.',
        badge: 'Transparence'
      },
      {
        title: 'Main-d’œuvre en journée',
        amount: 'Dès 65 € / h',
        details: 'Taux horaire standard (hors pièces de rechange). La première heure est entamée dès le début des réparations.',
        badge: 'Base indicative'
      },
      {
        title: 'Majoration astreinte (soir & week-end)',
        amount: '+50% à +100%',
        details: 'Appliquée sur la main-d’œuvre pour les interventions en soirée (après 18h), week-ends et jours fériés. Toujours confirmée au téléphone avant le départ du technicien.',
        badge: 'Selon horaire'
      }
    ],
    pricingNotes: [
      'Tarifs indiqués TVAC 6% pour les logements privés de plus de 10 ans (21% pour les logements de moins de 10 ans ou locaux commerciaux).',
      'Le coût total d’un dépannage dépend du temps passé et des pièces remplacées (raccords, robinetterie, tronçon de tuyau).',
      'Le technicien vous présente un devis détaillé sur place avant d’engager les travaux.'
    ],
    
    testimonialsSectionTitle: 'Retours de clients dépannés en urgence à Liège',
    testimonials: [
      {
        author: 'Marc D.',
        location: 'Liège (Quartier Outremeuse)',
        quote: 'Intervention rapide pour une rupture de canalisation dans ma cave un dimanche. Le technicien a immédiatement sécurisé l’installation avant de colmater la fuite. Facture conforme à ce qui m’avait été annoncé au téléphone.',
        service: 'Dépannage d’urgence (Rupture canalisation)',
        context: 'Intervention d’astreinte confirmée'
      },
      {
        author: 'Sophie L.',
        location: 'Seraing',
        quote: 'Très réactifs lors de notre appel. Le technicien a localisé le bouchon d’évacuation et résolu le problème sans abîmer nos tuyaux. Explication des prix claire avant de commencer.',
        service: 'Débouchage d’urgence',
        context: 'Intervention résidentielle'
      }
    ],
    
    coverageSectionTitle: 'Périmètre d’intervention d’urgence',
    coverageIntro: 'Nous intervenons en priorité dans la zone urbaine liégeoise et les communes adjacentes :',
    coverageTowns: LP_COMMON.coverageTowns,
    coverageDisclaimer: LP_COMMON.coverageDisclaimer,
    
    formSectionTitle: 'Vous préférez être rappelé ?',
    formSectionIntro: 'Pour une urgence avec écoulement continu, appelez directement le 0466 26 58 95. Pour un besoin rapide sans inondation, demandez un rappel ci-dessous :',
    formProblemOptions: [
      { value: 'fuite_active', label: 'Fuite d’eau active / robinet ou tuyau qui coule' },
      { value: 'wc_deborde', label: 'WC bouché avec risque de débordement' },
      { value: 'tuyau_casse', label: 'Tuyau percé, cassé ou fendu' },
      { value: 'refoulement_eaux', label: 'Refoulement d’eaux usées dans la maison' },
      { value: 'panne_eau_chaude', label: 'Panne d’eau chaude / boiler qui fuit' },
      { value: 'autre_urgence', label: 'Autre problème de plomberie urgent' }
    ],
    
    faqsSectionTitle: 'Questions fréquentes sur nos urgences plomberie',
    faqs: [
      {
        question: 'Quels types d’urgences de plomberie prenez-vous en charge ?',
        answer: 'Nous intervenons sur les fuites d’eau actives, tuyaux percés ou éclatés, WC bouchés avec risque de débordement, vannes d’arrêt générales défectueuses et pannes de chauffe-eau entraînant une fuite continue.'
      },
      {
        question: 'Quel est le délai réel d’arrivée chez moi à Liège ?',
        answer: 'Le délai varie selon la circulation routière et la disponibilité du technicien d’astreinte. Lors de votre appel au 0466 26 58 95, nous vérifions notre planning et vous donnons une estimation réaliste avant de déclencher l’intervention.'
      },
      {
        question: 'Comment fonctionnent les tarifs de nuit et de week-end ?',
        answer: 'Pour les interventions en dehors des heures ouvrées (en soirée après 18h, le samedi, le dimanche et les jours fériés), une majoration de 50% à 100% s’applique sur le taux horaire de main-d’œuvre. Ce supplément vous est systématiquement précisé au téléphone avant le départ du plombier.'
      },
      {
        question: 'Un devis est-il présenté avant le début des travaux ?',
        answer: 'Oui. Le technicien effectue d’abord un constat visuel sur place, identifie la panne et vous présente le devis chiffré comprenant le déplacement, la main-d’œuvre et les pièces éventuelles. Les travaux ne commencent qu’après votre accord.'
      },
      {
        question: 'Que dois-je faire en attendant l’arrivée du plombier ?',
        answer: 'Fermez immédiatement la vanne d’arrivée d’eau générale (souvent située près de votre compteur d’eau ou dans la cave). Si de l’eau s’approche de prises ou tableaux électriques, coupez le disjoncteur correspondant par précaution.'
      }
    ],
    
    finalCtaTitle: 'Une urgence plomberie en cours à Liège ?',
    finalCtaSubtext: 'Notre équipe est joignable pour sécuriser votre installation et intervenir dans les meilleurs délais.',
    finalCtaButtonText: 'Appeler le 0466 26 58 95'
  },
  
  'debouchage-liege': {
    slug: 'debouchage-liege',
    serviceCategory: 'debouchage',
    metaTitle: 'Débouchage Canalisation Liège | WC, Évier & Égout | Devis Avant Travaux',
    metaDescription: 'Débouchage de canalisation à Liège et environs : WC, évier, douche, égout. Dépannage mécanique et haute pression. Prix forfaitaire dès 140 €, devis expliqué avant travaux.',
    canonicalPath: '/lp/debouchage-liege/',
    heroBadge: 'Liège & environs • Débouchage mécanique & haute pression',
    heroH1: 'Débouchage canalisation à Liège',
    heroSubheadline: 'WC, évier, douche ou égout bouché. Appelez pour un diagnostic rapide et un débouchage adapté à vos conduites.',
    heroPrimaryCtaText: 'Appeler pour un débouchage : 0466 26 58 95',
    heroReassurance: 'Méthode et prix expliqués avant intervention. Matériel professionnel.',
    persistentBarCtaText: 'Débouchage : 0466 26 58 95',
    phoneNumberDisplay: LP_COMMON.phoneDisplay,
    phoneNumberTel: LP_COMMON.phoneTel,
    whatsappUrl: `${LP_COMMON.whatsappBase}?text=Bonjour%20Lynecares,%20j%27ai%20une%20canalisation%20bouch%C3%A9e%20%C3%A0%20Li%C3%A8ge%20:`,
    
    reassuranceStrip: [
      { icon: '🏷️', title: 'Forfait dès 140 €', subtitle: 'Prix de base annoncé d’emblée, sans surprise' },
      { icon: '⚙️', title: 'Matériel adapté', subtitle: 'Furet mécanique ou hydrocurage selon le bouchon' },
      { icon: '🔍', title: 'Contrôle d’écoulement', subtitle: 'Vérification du flux avant notre départ' }
    ],
    
    problemsSectionTitle: 'Quelle canalisation est bloquée chez vous ?',
    problemsSectionIntro: 'Un bouchon mal traité avec des produits chimiques corrosifs peut endommager vos tuyauteries. Nous intervenons avec du matériel professionnel pour une désobstruction durable.',
    problems: [
      {
        icon: '🚽',
        title: 'WC bouché & toilettes engorgées',
        description: 'L’eau monte dans la cuvette et menace de déborder. Dégagement soigné au furet électrique pour évacuer les bouchons de papier ou objets coincés sans rayer la faïence.',
        urgencyHint: 'Intervention courante'
      },
      {
        icon: '🍳',
        title: 'Évier de cuisine & siphon obstrué',
        description: 'Écoulement très lent, bruits de glouglou ou reflux d’eaux grasses. Dégraissage et nettoyage mécanique du siphon et de la conduite d’évacuation.',
        urgencyHint: 'Nettoyage en profondeur'
      },
      {
        icon: '🚿',
        title: 'Douche ou baignoire qui stagne',
        description: 'Accumulation de cheveux, résidus de savon et calcaire bloquant la bonde ou le siphon encastré sous receveur.',
        urgencyHint: 'Désobstruction ciblée'
      },
      {
        icon: '🏡',
        title: 'Égout principal & chambre de visite qui déborde',
        description: 'Refoulement général affectant plusieurs appareils de l’habitation ou la cave. Désobstruction des conduites extérieures vers le collecteur de voirie.',
        urgencyHint: 'Hydrocurage recommandé'
      },
      {
        icon: '👃',
        title: 'Remontées d’odeurs persistantes',
        description: 'Odeurs de fosse ou d’égout émanant des siphons. Diagnostic de la ventilation primaire ou des dépôts résiduels incrustés dans les parois.',
        urgencyHint: 'Diagnostic assainissement'
      }
    ],
    
    solutionsSectionTitle: 'Nos techniques de débouchage professionnel',
    solutionsSectionIntro: 'La méthode est choisie sur place après examen de l’accès et du diamètre des conduites. Tous les bouchons ne nécessitent pas la haute pression.',
    solutions: [
      {
        icon: '🌀',
        title: 'Débouchage mécanique au furet électrique',
        description: 'Câble flexible motorisé avec têtes spécifiques qui désagrège le bouchon sans risque pour le PVC, la fonte ou le grès.',
        equipment: 'Furet professionnel d’atelier'
      },
      {
        icon: '💦',
        title: 'Hydrocurage haute pression (conduites & égouts)',
        description: 'Nettoyage des parois par jets d’eau à haute pression pour éliminer les amas de graisse, boues et tartre dans les gros diamètres.',
        equipment: 'Hydrocureuse professionnelle'
      },
      {
        icon: '📹',
        title: 'Inspection par caméra vidéo (sur indication)',
        description: 'Utilisée lorsqu’un bouchon se reforme régulièrement ou en cas de suspicion d’affaissement, contre-pente ou pénétration de racines.',
        equipment: 'Caméra endoscopique étanche HD'
      },
      {
        icon: '✅',
        title: 'Test d’écoulement après intervention',
        description: 'Nous effectuons systématiquement des tests de charge en eau pour nous assurer que l’évacuation s’effectue à débit normal avant de quitter les lieux.',
        equipment: 'Contrôle qualité systématique'
      }
    ],
    
    processSectionTitle: 'Les étapes de notre intervention de débouchage',
    processSectionIntro: 'Une procédure claire pour rétablir votre évacuation sans dégrader vos installations :',
    processSteps: [
      {
        step: 1,
        title: '1. Diagnostic téléphonique',
        description: 'Nous identifions le type d’appareil touché (un seul sanitaire ou toute la maison) et convenons du rendez-vous ou de l’intervention d’urgence.',
        highlight: 'Identification de l’ampleur'
      },
      {
        step: 2,
        title: '2. Choix de la méthode & validation du prix',
        description: 'Sur place, le technicien vérifie l’accès et vous propose la solution la plus économique et efficace (mécanique ou hydrocurage) avec devis ferme.',
        highlight: 'Devis validé avant action'
      },
      {
        step: 3,
        title: '3. Débouchage & contrôle d’évacuation',
        description: 'Le bouchon est extrait ou désagrégé, la conduite rincée et le bon écoulement validé sous vos yeux.',
        highlight: 'Résultat vérifié ensemble'
      }
    ],
    
    pricingSectionTitle: 'Grille tarifaire indicative pour le débouchage',
    pricingSectionIntro: 'Nos tarifs de débouchage sont forfaitaires pour les interventions courantes, sans surprise à la fin :',
    pricingItems: [
      {
        title: 'Débouchage canalisation (forfait de base)',
        amount: 'Dès 140 €',
        details: 'Comprend la désobstruction mécanique courante (WC, évier, douche) avec outillage professionnel standard.',
        badge: 'Forfait courant'
      },
      {
        title: 'Frais de déplacement',
        amount: '45 €',
        details: 'Applicable sur Liège et sa périphérie immédiate lorsque non inclus dans une formule forfaitaire spécifique.',
        badge: 'Déplacement'
      },
      {
        title: 'Hydrocurage / Inspection caméra',
        amount: 'Sur devis préalable',
        details: 'Pour les réseaux extérieurs complexes, égouts entartrés ou récidives nécessitant du matériel lourd.',
        badge: 'Si justifié'
      }
    ],
    pricingNotes: [
      'Montants exprimés TVAC 6% pour les habitations privées de plus de 10 ans (21% si moins de 10 ans ou locaux professionnels).',
      'Le forfait de base couvre la désobstruction standard. Si une anomalie structurelle (tuyau écrasé, racine pénétrante) est découverte, un devis de réparation vous est soumis avant toute suite.',
      'Majoration de soirée (après 18h) et de week-end applicable en cas d’astreinte urgente, confirmée lors de votre appel.'
    ],
    
    testimonialsSectionTitle: 'Avis de clients pour des débouchages à Liège',
    testimonials: [
      {
        author: 'Sophie L.',
        location: 'Seraing',
        quote: 'Très professionnels. Ils ont localisé un bouchon récalcitrant dans nos évacuations sans devoir casser le carrelage. Travail propre, rapide et explications claires.',
        service: 'Débouchage d’évacuation',
        context: 'Intervention sur canalisation domestique'
      },
      {
        author: 'Marc D.',
        location: 'Liège (Outremeuse)',
        quote: 'WC bouché un samedi matin. Déplacement rapide, technicien courtois qui a utilisé un furet motorisé efficace. Facture conforme au tarif communiqué au téléphone.',
        service: 'Débouchage WC d’urgence',
        context: 'Dépannage d’astreinte'
      }
    ],
    
    coverageSectionTitle: 'Secteurs desservis pour le débouchage',
    coverageIntro: 'Nos techniciens interviennent dans toute l’agglomération liégeoise :',
    coverageTowns: LP_COMMON.coverageTowns,
    coverageDisclaimer: LP_COMMON.coverageDisclaimer,
    
    formSectionTitle: 'Besoin d’un débouchage ou d’un conseil ?',
    formSectionIntro: 'Pour un refoulement urgent, appelez immédiatement le 0466 26 58 95. Pour planifier une intervention dans la journée, remplissez cette demande de rappel :',
    formProblemOptions: [
      { value: 'wc_bouche', label: 'WC / toilettes complètement bouchées' },
      { value: 'evier_cuisine', label: 'Évier de cuisine / siphon bloqué' },
      { value: 'douche_baignoire', label: 'Douche ou baignoire qui ne s’évacue plus' },
      { value: 'egout_chambre_visite', label: 'Égout principal / chambre de visite extérieure' },
      { value: 'odeurs_refoulement', label: 'Refoulement général ou fortes odeurs' },
      { value: 'autre_debouchage', label: 'Autre canalisation bouchée' }
    ],
    
    faqsSectionTitle: 'Questions fréquentes sur le débouchage à Liège',
    faqs: [
      {
        question: 'Quels équipements sanitaires pouvez-vous déboucher ?',
        answer: 'Nous prenons en charge les WC, siphons d’éviers, colonnes de cuisine, receveurs de douche, baignoires, colonnes d’eaux usées d’immeubles, ainsi que les égouts et chambres de visite extérieures.'
      },
      {
        question: 'Comment choisissez-vous la méthode de débouchage ?',
        answer: 'Le technicien examine d’abord la nature de la canalisation et l’emplacement du bouchon. Pour un sanitaire intérieur, le furet mécanique est généralement privilégié pour préserver les tuyaux. Pour un égout extérieur encrassé par des graisses ou boues, l’hydrocurage haute pression est plus indiqué.'
      },
      {
        question: 'L’inspection par caméra est-elle obligatoire ?',
        answer: 'Non, elle n’est pas systématique. Nous ne la conseillons que si les bouchons se répètent anormalement au même endroit ou si le furet bute sur un obstacle suspect (tuyau fendu, écrasement, racines).'
      },
      {
        question: 'Que comprend le forfait de débouchage à partir de 140 € ?',
        answer: 'Il comprend l’intervention de désobstruction mécanique avec outillage professionnel pour un bouchon courant. Le tarif exact et les frais de déplacement associés vous sont toujours confirmés avant de commencer.'
      },
      {
        question: 'Que se passe-t-il si la canalisation est cassée sous terre ?',
        answer: 'Si le matériel détecte une casse ou un affaissement structurel de la conduite, nous stoppons l’intervention pour éviter d’aggraver la situation et vous remettons un diagnostic avec devis pour la réparation ou le terrassement nécessaire.'
      }
    ],
    
    finalCtaTitle: 'Votre évacuation est bloquée à Liège ?',
    finalCtaSubtext: 'Contactez notre service de débouchage pour une intervention rapide avec du matériel professionnel adapté.',
    finalCtaButtonText: 'Appeler pour un débouchage : 0466 26 58 95'
  },
  
  'fuite-depannage-liege': {
    slug: 'fuite-depannage-liege',
    serviceCategory: 'fuite_depannage',
    metaTitle: 'Réparation de Fuite d’Eau Liège | Robinet, Chasse WC, Tuyau | Lynecares',
    metaDescription: 'Réparation rapide de fuite d’eau à Liège : robinet, chasse d’eau, siphon, raccord ou tuyau percé. Devis avant réparation et test d’étanchéité garanti. Appel 0466 26 58 95.',
    canonicalPath: '/lp/fuite-depannage-liege/',
    heroBadge: 'Liège & communes limitrophes • Devis clair & test d’étanchéité',
    heroH1: 'Réparation de fuite à Liège',
    heroSubheadline: 'Robinet, chasse WC, siphon ou tuyau qui fuit. Appelez pour organiser le diagnostic et la réparation par un artisan local.',
    heroPrimaryCtaText: 'Appeler pour une fuite : 0466 26 58 95',
    heroReassurance: 'Devis avant réparation et contrôle de l’étanchéité après intervention.',
    persistentBarCtaText: 'Réparer une fuite : 0466 26 58 95',
    phoneNumberDisplay: LP_COMMON.phoneDisplay,
    phoneNumberTel: LP_COMMON.phoneTel,
    whatsappUrl: `${LP_COMMON.whatsappBase}?text=Bonjour%20Lynecares,%20j%27ai%20une%20fuite%20d%27eau%20%C3%A0%20Li%C3%A8ge%20:`,
    
    reassuranceStrip: [
      { icon: '🔍', title: 'Diagnostic transparent', subtitle: 'Origine de la fuite identifiée avec précision' },
      { icon: '📝', title: 'Devis avant travaux', subtitle: 'Prix des pièces et main-d’œuvre fixé avant pose' },
      { icon: '💧', title: 'Contrôle d’étanchéité', subtitle: 'Test sous pression effectué avant notre départ' }
    ],
    
    problemsSectionTitle: 'Fuites d’eau courantes que nous réparons',
    problemsSectionIntro: 'Même un goutte-à-goutte discret peut gaspiller des centaines de litres et causer des dégradations insidieuses dans vos murs et plafonds.',
    problems: [
      {
        icon: '🚰',
        title: 'Robinet ou mitigeur qui goutte en continu',
        description: 'Cartouche céramique usée, tête de robinet entartrée ou flexible percé sous vasque. Remplacement de cartouche ou pose d’une nouvelle robinetterie.',
        urgencyHint: 'Économie d’eau immédiate'
      },
      {
        icon: '🚽',
        title: 'Chasse d’eau de WC qui coule',
        description: 'Le flotteur ne coupe plus l’eau ou le joint de cloche est déformé par le calcaire. Jusqu’à 150 litres gaspillés par jour sans réparation.',
        urgencyHint: 'Mécanisme réparé sur place'
      },
      {
        icon: '🥣',
        title: 'Fuite sous évier, lavabo ou siphon',
        description: 'Joint silicone défaillant, raccord PVC desserré ou siphon fendu provoquant des infiltrations sous les meubles de cuisine ou de salle de bain.',
        urgencyHint: 'Remplacement de raccords'
      },
      {
        icon: '🧱',
        title: 'Tache d’humidité sur un mur ou plafond',
        description: 'Infiltration provenant de l’étage supérieur (joints de baignoire, canalisation d’évacuation ou raccord encastré défectueux).',
        urgencyHint: 'Localisation de l’origine'
      },
      {
        icon: '🔩',
        title: 'Tuyau cuivre, Alpex ou vanne d’arrêt qui suinte',
        description: 'Corrosion, raccord usé ou microfissure sur la tuyauterie d’alimentation générale ou de chauffage.',
        urgencyHint: 'Sertissage ou brasure'
      }
    ],
    
    solutionsSectionTitle: 'Nos interventions de réparation et dépannage',
    solutionsSectionIntro: 'Nous intervenons sur les équipements sanitaires visibles et les sections accessibles avec des composants de qualité professionnelle.',
    solutions: [
      {
        icon: '🔧',
        title: 'Remplacement de robinetterie et cartouches',
        description: 'Pose de mitigeurs agréés Belgaqua, changement de têtes, flexibles blindés inox et joints fibre/toriques de haute résistance.',
        equipment: 'Composants agréés & certifiés'
      },
      {
        icon: '🚽',
        title: 'Remise en état de mécanismes de WC',
        description: 'Remplacement de flotteurs universels silencieux, mécanismes à double poussoir pour économie d’eau et joints de cuvette.',
        equipment: 'Mécanismes Geberit / Siamp compatibles'
      },
      {
        icon: '📐',
        title: 'Réparation de tuyauterie cuivre & multicouche',
        description: 'Découpe de la section endommagée, sertissage de manchons Alpex ou brasure cuivre pour une étanchéité définitive.',
        equipment: 'Pince à sertir pro & chalumeau'
      },
      {
        icon: '🔍',
        title: 'Distinction fuite visible vs recherche non destructive',
        description: 'Réparation directe pour les fuites localisées. Pour une fuite invisible encastrée dans une dalle sans repère, nous fixons un diagnostic spécifique.',
        equipment: 'Examen méthodologique clair'
      }
    ],
    
    processSectionTitle: 'Notre méthode de dépannage de fuite',
    processSectionIntro: 'Un déroulement étape par étape pour remettre votre installation en conformité :',
    processSteps: [
      {
        step: 1,
        title: '1. Conseil immédiat & coupure d’eau',
        description: 'Dès votre appel au 0466 26 58 95, nous vous guidons pour isoler la fuite si elle menace vos biens et convenons du passage.',
        highlight: 'Mise en sécurité guidée'
      },
      {
        step: 2,
        title: '2. Examen visuel sur place & devis',
        description: 'Le plombier inspecte le sanitaire ou la tuyauterie en cause, identifie les pièces défaillantes et vous remet un devis précis.',
        highlight: 'Chiffrage avant démontage'
      },
      {
        step: 3,
        title: '3. Remplacement & test d’étanchéité sous pression',
        description: 'Remplacement des pièces usées, remise sous pression du circuit et vérification scrupuleuse des jonctions avant clôture.',
        highlight: 'Contrôle étanchéité certifié'
      }
    ],
    
    pricingSectionTitle: 'Tarifs de réparation de fuite',
    pricingSectionIntro: 'Une tarification transparente basée sur nos coûts réels de déplacement et de main-d’œuvre :',
    pricingItems: [
      {
        title: 'Main-d’œuvre en journée',
        amount: 'Dès 65 € / h',
        details: 'Taux horaire standard pour l’intervention de réparation (hors pièces de rechange nécessaires).',
        badge: 'Base indicative'
      },
      {
        title: 'Frais de déplacement',
        amount: '45 €',
        details: 'Applicable sur Liège et sa périphérie immédiate pour le déplacement de l’artisan avec outillage complet.',
        badge: 'Déplacement'
      },
      {
        title: 'Pièces de rechange sanitaires',
        amount: 'Selon devis sur place',
        details: 'Mécanismes WC, cartouches céramiques, siphons ou raccords facturés au prix juste selon le modèle installé.',
        badge: 'Sur devis'
      }
    ],
    pricingNotes: [
      'Montants indiqués TVAC 6% pour les bâtiments résidentiels privés de plus de 10 ans (21% si moins de 10 ans ou usage professionnel).',
      'Le coût final comprend le déplacement, le temps effectif passé et les composants de plomberie remplacés.',
      'Aucun travail n’est réalisé sans la validation préalable de notre devis sur place.'
    ],
    
    testimonialsSectionTitle: 'Avis de clients pour des réparations à Liège',
    testimonials: [
      {
        author: 'Marc D.',
        location: 'Liège (Outremeuse)',
        quote: 'Dépannage d’une fuite importante sous mon évier qui risquait d’abîmer les meubles neufs. Le technicien a remplacé le siphon et deux raccords en moins d’une heure. Très propre.',
        service: 'Réparation de fuite sous évier',
        context: 'Dépannage plomberie'
      },
      {
        author: 'Jean-Pol',
        location: 'Chaudfontaine',
        quote: 'Artisan ponctuel et sérieux. Réparation d’une chasse d’eau encastrée qui fuyait depuis des semaines. Travail soigné et facture sans surprise.',
        service: 'Réparation mécanisme WC',
        context: 'Intervention sanitaire'
      }
    ],
    
    coverageSectionTitle: 'Zone de déplacement pour vos fuites',
    coverageIntro: 'Nous intervenons rapidement à Liège et dans les communes voisines :',
    coverageTowns: LP_COMMON.coverageTowns,
    coverageDisclaimer: LP_COMMON.coverageDisclaimer,
    
    formSectionTitle: 'Une fuite à réparer ? Demandez un rappel',
    formSectionIntro: 'Pour une fuite abondante menaçant vos locaux, coupez l’eau et appelez directement le 0466 26 58 95. Pour un goutte-à-goutte ou une demande de devis, remplissez ce formulaire :',
    formProblemOptions: [
      { value: 'fuite_robinet', label: 'Robinet ou mitigeur qui goutte' },
      { value: 'fuite_chasse_wc', label: 'Chasse d’eau de WC qui coule en continu' },
      { value: 'fuite_sous_evier', label: 'Fuite sous évier / lavabo / siphon' },
      { value: 'tuyau_perce', label: 'Tuyau d’eau ou raccord qui suinte' },
      { value: 'tache_humidite', label: 'Tache d’humidité / suspicion de fuite' },
      { value: 'autre_fuite', label: 'Autre fuite ou dépannage de plomberie' }
    ],
    
    faqsSectionTitle: 'Questions fréquentes sur la réparation de fuites',
    faqs: [
      {
        question: 'Quelles fuites pouvez-vous réparer en urgence ?',
        answer: 'Nous intervenons sur les fuites de robinetterie, de mécanismes de WC, de siphons, de vannes d’arrêt défaillantes, ainsi que sur les ruptures de conduites d’eau visibles (cuivre, Alpex, acier galvanisé).'
      },
      {
        question: 'Faites-vous la différence entre réparation de fuite et détection spécialisée ?',
        answer: 'Oui. Une réparation directe concerne une fuite visible ou accessible (sanitaire, raccord apparent). Lorsqu’une fuite est totalement invisible (encastrée sous dalle sans signe extérieur), un diagnostic par recherche de fuite non destructive peut être programmé sur rendez-vous.'
      },
      {
        question: 'Comment est calculé le prix d’une réparation de fuite ?',
        answer: 'Le prix se compose du forfait déplacement (45 € sur Liège et environs), du temps de main-d’œuvre (base à partir de 65 €/h) et du coût des pièces de plomberie remplacées. Le devis complet vous est toujours présenté avant toute réparation.'
      },
      {
        question: 'Vérifiez-vous l’étanchéité après avoir réparé la fuite ?',
        answer: 'Oui, c’est une obligation professionnelle. Nous remettons le circuit sous pression et vérifions l’absence totale de suintement avec un papier témoin ou manomètre avant de vous faire constater la réparation.'
      },
      {
        question: 'Fournissez-vous un document pour mon assurance habitation ?',
        answer: 'Oui. En cas de sinistre ou dégât des eaux couvert par votre contrat, nous vous délivrons une facture détaillée mentionnant clairement la nature de la fuite, l’origine de la panne et les réparations effectuées.'
      }
    ],
    
    finalCtaTitle: 'Une fuite d’eau à faire réparer à Liège ?',
    finalCtaSubtext: 'Ne laissez pas les dégâts s’étendre. Contactez nos artisans locaux pour un diagnostic et une réparation durable.',
    finalCtaButtonText: 'Appeler pour une fuite : 0466 26 58 95'
  }
};
