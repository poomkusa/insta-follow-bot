/*
- Go to your profile on instagram.com (sign in if not already)
- Click on `XXX following` for the popup with the users you're following to appear
- Open Chrome Devtools and Paste the following into the Console and hit return:
*/

(async function(){
  const UNFOLLOW_LIMIT = 100
  const delay = (ms) => new Promise(_ => setTimeout(_, ms))
  const findButton = (txt) => [...document.querySelectorAll("button").entries()].map(([pos, btn]) => btn).filter(btn => btn.innerHTML === txt)[0]

  console.log("Start")
  for (let i = 0; i < UNFOLLOW_LIMIT; i++) {
    const $next = findButton("Following")          
    if (!$next) { continue }
    $next.scrollIntoViewIfNeeded()  
    $next.click()
    await delay(100)
    $confirm = findButton("Unfollow")    
    if ($confirm) {
      $confirm.click()
    }

    await delay(240 * 1000) // Wait 240s, 15 unfollows per hour limit
    console.log(`Unfollowed #${i}`)
  }

  console.log("The end")
})()
