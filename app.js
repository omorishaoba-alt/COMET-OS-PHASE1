const { Document, Packer, Paragraph, ImageRun } = docx;

document.getElementById("receiptForm").onsubmit = async (e) => {
  e.preventDefault();

  const name = nameInput.value;
  const id = idInput.value;
  const asset = assetInput.value;
  const timestamp = new Date().toISOString();

  const payload = {
    name,
    id,
    asset,
    timestamp,
    issuer: "FSTL OS v1.0"
  };

  const qrCanvas = document.getElementById("qr");
  await QRCode.toCanvas(qrCanvas, JSON.stringify(payload));

  document.getElementById("download").onclick = async () => {
    const image = qrCanvas.toDataURL("image/png");

    const doc = new Document({
      sections: [{
        children: [
          new Paragraph(`FSTL OS VERIFICATION RECEIPT`),
          new Paragraph(`Name: ${name}`),
          new Paragraph(`ID: ${id}`),
          new Paragraph(`Asset: ${asset}`),
          new Paragraph(`Timestamp: ${timestamp}`),
          new Paragraph(` `),
          new Paragraph({
            children: [new ImageRun({
              data: image,
              transformation: { width: 200, height: 200 }
            })]
          })
        ]
      }]
    });

    const blob = await Packer.toBlob(doc);
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = `FSTL_Verification_${name}.docx`;
    a.click();
  };
};
