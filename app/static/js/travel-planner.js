document.getElementById('tripForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    // Show loading spinner and results card
    document.getElementById('loadingSpinner').style.display = 'block';
    document.getElementById('resultsCard').style.display = 'block';
    document.getElementById('resultsContent').innerHTML = '';

    const formData = new FormData(this);
    const city = formData.get('city');
    const days = parseInt(formData.get('days'));
    const attractionsPerDay = parseInt(formData.get('attractions_per_day'));

    try {
        // Simulate API call with a delay
        await new Promise(resolve => setTimeout(resolve, 2000));
        
        // Simulate API response data
        const data = {
            city: city,
            days: days,
            daily_plans: []
        };
        
        // Create simple daily plans
        for (let i = 1; i <= days; i++) {
            const attractions = [];
            for (let j = 1; j <= attractionsPerDay; j++) {
                attractions.push({
                    name: `${city} Attraction ${j}`,
                    category: "Tourist Spot",
                    estimated_duration: "2 hours",
                    // address is sometimes missing
                    address: j % 2 === 0 ? `Some Street` : undefined,
                    description: `Description for attraction ${j} in ${city}.`
                });
            }
            
            data.daily_plans.push({
                day_number: i,
                attractions: attractions,
                // meal_suggestions is sometimes missing
                meal_suggestions: i % 2 === 0 ? [
                    `Breakfast at ${city} Café`,
                    `Lunch at ${city} Bistro`,
                    `Dinner at ${city} Restaurant`
                ] : undefined
            });
        }

        // overall_tips is sometimes missing
        if (days % 2 === 0) {
            data.overall_tips = `Travel tips for ${city}: Bring comfortable shoes and a map.`;
        }

        // Display the itinerary
        let html = '<div class="itinerary">';
        if (data.daily_plans && Array.isArray(data.daily_plans)) {
            data.daily_plans.forEach((day) => {
                html += `
                    <div class="day-plan">
                        <h6>Day ${day.day_number}</h6>
                        <ul>
                            ${day.attractions.map(attraction => `
                                <li>
                                    <strong>${attraction.name}</strong><br>
                                    ${attraction.category} • <small>${attraction.estimated_duration}</small><br>
                                    ${attraction.address ? `<small>${attraction.address}</small><br>` : ''}
                                    ${attraction.description}
                                </li>
                            `).join('')}
                        </ul>
                        ${day.meal_suggestions && Array.isArray(day.meal_suggestions) && day.meal_suggestions.length ? `
                            <div>
                                <p>Meal Suggestions:</p>
                                <ul>
                                    ${day.meal_suggestions.map(suggestion => `
                                        <li>${suggestion}</li>
                                    `).join('')}
                                </ul>
                            </div>
                        ` : ''}
                    </div>
                `;
            });
            
            // Only show overall tips if they exist
            if (data.overall_tips) {
                html += `
                    <div>
                        <h6>Overall Tips</h6>
                        <div>
                            ${data.overall_tips}
                        </div>
                    </div>
                `;
            }
        } else {
            html += '<div>No itinerary data available</div>';
        }
        html += '</div>';
        document.getElementById('resultsContent').innerHTML = html;
    } catch (error) {
        document.getElementById('resultsContent').innerHTML = `
            <div>
                An error occurred while planning your trip. Please try again.
            </div>
        `;
    } finally {
        // Hide loading spinner
        document.getElementById('loadingSpinner').style.display = 'none';
    }
});
