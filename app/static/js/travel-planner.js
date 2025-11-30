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
                    <!-- Added mb-4 for margin-bottom spacing between days -->
                    <div class="day-plan mb-4">
                        <h6>Day ${day.day_number}</h6>
                        <!-- Replaced basic ul with Bootstrap's list-group component -->
                        <ul class="list-group">
                            ${day.attractions.map(attraction => `
                                <!-- list-group-item adds borders, padding, and hover states -->
                                <li class="list-group-item">
                                    <strong>${attraction.name}</strong><br>
                                    <!-- Added text-muted class to de-emphasize secondary information -->
                                    <small class="text-muted">${attraction.category} • ${attraction.estimated_duration}</small><br>
                                    ${attraction.address ? `<small class="text-muted">${attraction.address}</small><br>` : ''}
                                    ${attraction.description}
                                </li>
                            `).join('')}
                        </ul>
                    ${day.meal_suggestions ? `
                        <!-- Added mt-2 for margin-top spacing -->
                        <div class="mt-2">
                            <!-- Used text-muted for consistent styling of secondary headers -->
                            <small class="text-muted">Meal Suggestions:</small>
                            <!-- list-unstyled removes default bullet points for cleaner design -->
                                <ul class="list-group">
                                    ${day.meal_suggestions.map(suggestion => `
                                        <li class="list-group-item>• ${suggestion}</li>
                                `).join('')}
                            </ul>
                        </div>
                    ` : ''}
                </div>
            `;
        });
        
        if (data.overall_tips) {
            html += `
                <!-- Added overall-tips class for potential custom styling and mt-4 for spacing -->
                <div class="overall-tips mt-4">
                    <h6>Overall Tips</h6>
                    <!-- Used Bootstrap's alert component with info styling -->
                    <div class="alert alert-info">
                        ${data.overall_tips}
                    </div>
                </div>
            `;
        }
    } else {
        // <!-- Used Bootstrap's alert component with warning styling for empty states -->
        html += '<div class="alert alert-warning">No itinerary data available</div>';
    }
    html += '</div>';
    document.getElementById('resultsContent').innerHTML = html;
    } catch (error) {
        // <!-- Used Bootstrap's alert component with danger styling for errors -->
        document.getElementById('resultsContent').innerHTML = `
            <div class="alert alert-danger">
                An error occurred while planning your trip. Please try again.
            </div>
        `;
    } finally {
        // Hide loading spinner
        document.getElementById('loadingSpinner').style.display = 'none';
    }
});
