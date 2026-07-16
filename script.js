const constitutionContent = [
    {
        clause: '1.1',
        title: 'Membership and Admission',
        text: 'Membership is open to Administration Police Officers recruited in 2005, subject to character evaluation. Membership is capped at 115 members and new admissions require approval by two-thirds of the existing members.',
    },
    {
        clause: '1.2',
        title: 'Membership Fees',
        text: 'New members pay a non-refundable registration fee of Ksh 1,000, plus the amount already paid by an existing member, and Ksh 5,000 for each year the association has existed.',
    },
    {
        clause: '2.1',
        title: 'Monthly Contributions',
        text: 'Every member shall contribute Ksh 1,000 between the 20th and 27th of each month. Payments made between the 28th and 30th attract a 20% fine.',
    },
    {
        clause: '3.1',
        title: 'Termination of Membership',
        text: 'Membership may be terminated for non-payment of monthly contributions for three consecutive months after written notice. Membership may also terminate for failure to follow the constitution, rules, or attend meetings.',
    },
    {
        clause: '4.1',
        title: 'Finance and Assets',
        text: 'The association funds may only be used to safeguard members’ interests and are derived from monthly contributions, fees, loans, and investments. All bank accounts and financial documents are available for member scrutiny.',
    },
    {
        clause: '5.1',
        title: 'Executive Committee',
        text: 'The executive committee includes Chairperson, Secretary, Treasurer, Overseer, Investment Advisors, Regional Representatives, and Supervisory Committee members. The committee manages meetings, funds, and governance duties.',
    },
    {
        clause: '6.1',
        title: 'Audit and Transparency',
        text: 'An auditor is appointed each year by the AGM. A consolidated audited account is presented annually to the general meeting, and all financial records must be available for scrutiny.',
    },
];

function renderSearchResults(results, query) {
    const container = document.getElementById('constitutionResults');
    if (!container) return;

    container.innerHTML = '';

    if (!query) {
        container.innerHTML = '<div class="constitution-card"><h3>Start searching</h3><p>Type a term like "contributions", "membership", "audit", or "executive" to find relevant constitution passages.</p></div>';
        return;
    }

    if (results.length === 0) {
        container.innerHTML = '<div class="constitution-card"><h3>No results found</h3><p>Try another keyword like "fine", "governance", "security", or "finance".</p></div>';
        return;
    }

    results.forEach(item => {
        const card = document.createElement('div');
        card.className = 'constitution-card';
        card.innerHTML = `
            <div class="constitution-meta">
                <span class="clause-badge">Clause ${item.clause}</span>
            </div>
            <h3>${item.title}</h3>
            <p>${item.text}</p>
        `;
        container.appendChild(card);
    });
}

document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('constitutionSearch');
    const initialQuery = '';
    renderSearchResults([], initialQuery);

    if (searchInput) {
        searchInput.addEventListener('input', function (event) {
            const query = event.target.value.trim().toLowerCase();
            const results = constitutionContent.filter(item => {
                return item.title.toLowerCase().includes(query) || item.text.toLowerCase().includes(query);
            }).map(item => {
                const safeQuery = query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
                const highlightedText = query
                    ? item.text.replace(new RegExp(`(${safeQuery})`, 'gi'), '<mark>$1</mark>')
                    : item.text;

                return {
                    clause: item.clause,
                    title: item.title,
                    text: highlightedText,
                };
            });

            renderSearchResults(results, query);
        });
    }
});
