// write a function which formats a duration, given as a number of seconds, in a human-friendly way.
// The function must accept a non-negative integer. If it is zero, it just returns "now". 
// Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

function formatDuration (seconds) {
    
    const time = { years: 0 , days: 0 , hours: 0 , minutes: 0 , seconds: 0 }

    for ( var i = 0; i < seconds; i++ ) {

        // Seconds
        if ( time['seconds'] <= 59 ) {
            time['seconds'] += 1
        }

        // Minutes
        if ( time['seconds'] === 60 ) {
            time['minutes'] += 1
            time['seconds'] = 0
        }

        // Hours
        if ( time['minutes'] === 60 ) {
            time['hours'] += 1
            time['minutes'] = 0
            time['seconds'] = 0

        }

        // Days
        if ( time['hours'] === 24 ) {
            time['days'] += 1
            time['hours'] = 0
            time['minutes'] = 0
            time['seconds'] = 0

        }

        //Years
        if ( time['days'] === 365 ) {
            time['years'] += 1
            time['days'] = 0
            time['hours'] = 0
            time['minutes'] = 0
            time['seconds'] = 0

        }

    }

    // console.log( time['years'] , time['days'] , time['hours'] , time['minutes'] , time['seconds'] )
    let answer = []

    time['years'] === 0 ? null : time['years'] >= 2 ? answer.push( `${time['years']} years` ) : answer.push( `${time['years']} year` )
    time['days'] === 0 ? null : time['days'] >= 2 ? answer.push( `${time['days']} days` ) : answer.push( `${time['days']} day` )
    time['hours'] === 0 ? null : time['hours'] >= 2 ? answer.push( `${time['hours']} hours` ) : answer.push( `${time['hours']} hour` )
    time['minutes'] === 0 ? null : time['minutes'] >= 2 ? answer.push( `${time['minutes']} minutes` ) : answer.push( `${time['minutes']} minute` )
    time['seconds'] === 0 ? null : time['seconds'] >= 2 ? answer.push( `${time['seconds']} seconds` ) : answer.push( `${time['seconds']} second` )

    if ( answer.length === 0 ) {
        console.log( 'Now' )
        return 'now'
    } else if ( answer.length === 1 ) {
        console.log( answer[0] )
        return answer[0]
    } else if ( answer.length === 2 ) {
        console.log( answer.join(' and ') )
        return answer.join(' and ')
    } else if ( answer.length === 3 ) {
        console.log( `${answer[0]}, ${answer[1]} and ${answer[2]}` )
        return `${answer[0]}, ${answer[1]} and ${answer[2]}`
    } else if ( answer.length === 4 ) {
        console.log( `${answer[0]}, ${answer[1]}, ${answer[2]} and ${answer[3]}` )
        return `${answer[0]}, ${answer[1]}, ${answer[2]} and ${answer[3]}`
    } else {
        console.log( `${answer[0]}, ${answer[1]}, ${answer[2]}, ${answer[3]} and ${answer[4]}` )
        return `${answer[0]}, ${answer[1]}, ${answer[2]}, ${answer[3]} and ${answer[4]}`
    }

}

// TESTS
// formatDuration(1)          // "1 second"
// formatDuration(2)          // "2 seconds"
// formatDuration(60)         // "1 minute"
// formatDuration(62)         // "1 minute and 2 seconds"
// formatDuration(120)        // "2 minutes"
// formatDuration(3600)       // "1 hour"
// formatDuration(3662)       // "1 hour, 1 minute and 2 seconds"
// formatDuration(86400)      // 1 day
// formatDuration(129600)     // 1 day and 12 hours
// formatDuration(31536000)   // 1 year