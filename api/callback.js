/**
 * Vercel Serverless Function: Lead Callback Handler
 * Receives callback requests securely on the server side.
 * Keeps credentials, recipient emails, and webhook URLs completely out of client-side code.
 */
export default async function handler(req, res) {
  // CORS & Methods check
  if (req.method !== 'POST') {
    res.setHeader('Allow', ['POST']);
    return res.status(405).json({ error: 'Method Not Allowed' });
  }

  try {
    const body = typeof req.body === 'string' ? JSON.parse(req.body) : req.body;
    const { phone, location, problemType, description, serviceCategory, _lp_honey } = body || {};

    // 1. Silent anti-bot honeypot check
    if (_lp_honey && _lp_honey.trim() !== '') {
      return res.status(200).json({ success: true, message: 'Demande traitée' });
    }

    // 2. Strict server-side validation
    const cleanPhone = (phone || '').replace(/[\s\.\-\/]/g, '');
    if (!phone || cleanPhone.length < 8) {
      return res.status(400).json({ error: 'Numéro de téléphone invalide' });
    }

    if (!location || location.trim().length < 2) {
      return res.status(400).json({ error: 'Commune ou code postal requis' });
    }

    if (!problemType) {
      return res.status(400).json({ error: 'Type de problème requis' });
    }

    // 3. Payload preparation
    const leadRecord = {
      receivedAt: new Date().toISOString(),
      serviceCategory: serviceCategory || 'non_specifie',
      phone: phone.trim(),
      location: location.trim(),
      problemType: problemType.trim(),
      description: (description || '').trim().slice(0, 500)
    };

    // 4. Secure forwarding if webhook/email environment variables are configured
    const webhookUrl = process.env.LEAD_WEBHOOK_URL;
    if (webhookUrl) {
      try {
        await fetch(webhookUrl, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(leadRecord)
        });
      } catch (webhookErr) {
        console.error('[Callback Webhook Error]', webhookErr);
      }
    }

    // 5. Successful response
    return res.status(200).json({
      success: true,
      message: 'Demande de rappel enregistrée avec succès'
    });
  } catch (err) {
    console.error('[Callback Server Error]', err);
    return res.status(500).json({
      error: 'Erreur interne du serveur lors du traitement de la demande'
    });
  }
}
