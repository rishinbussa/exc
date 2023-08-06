function calculateCoolingLoad(event) {
    event.preventDefault();

    const area = parseFloat(document.getElementById('area').value);
    const occupants = parseInt(document.getElementById('occupants').value);
    const buildingType = document.getElementById('buildingType').value;
    const outdoorTemp = parseFloat(document.getElementById('outdoorTemp').value);
    const indoorTemp = parseFloat(document.getElementById('indoorTemp').value);

    const coolingLoad = buildingType === 'residential' ? 100 * occupants : 150 * occupants;
    const overallHeatTransferCoefficient = 30; 
    const qConduction = overallHeatTransferCoefficient * area * (outdoorTemp - indoorTemp);
    const sensibleCoolingLoad = qConduction + coolingLoad;

    const resultElement = document.getElementById('result');
    resultElement.textContent = `The sensible cooling load is: ${sensibleCoolingLoad} W`;
}
