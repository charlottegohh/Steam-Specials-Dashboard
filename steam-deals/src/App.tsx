import { useState } from "react"
import axios from 'axios'
import { ArrowUpDown } from 'lucide-react'

function App(){
  type Deal = {
    title: string
    discount: string
    original_price: string
    price: string
  }
  const[deals, setDeals] = useState<Deal[]>([])
  const[loading, setLoading] = useState(false)
  const[sortDirection, setSortDirection] = useState('asc')
  
  async function fetchDeals(){
    setLoading(true)
    const res = await axios.get('https://steam-discount-tracker.onrender.com/deals')
    console.log(res.data)
    setDeals(res.data)
    setLoading(false)
  }

  async function sortDeals(){
    const sortedDeals = [...deals].sort((a,b) => {
      if (sortDirection == 'asc'){
        return parseInt(a.discount)-parseInt(b.discount)
      }else{
        return parseInt(b.discount)-parseInt(a.discount)
      }
    })
    setDeals(sortedDeals)
    }

  return( 
    <div className="min-h-screen bg-grey px-6 py-10">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-3xl font-bold text-primary mb-1">Steam Deals</h1>
        <p className="text-primary text-sm mb-6">Latest Discounts from Steam Specials</p>
      <div className="flex items-center gap-3 mb-8">
        <button 
          onClick={fetchDeals}
          className="bg-dark text-primary text-sm px-5 py-2 rounded-lg hover:bg-dark-hover transition"
        >
          {loading ? 'Fetching...' : 'Fetch Deals' }
        </button>

        <button
          onClick={() => { 
          setSortDirection(sortDirection === 'asc' ? 'desc' : 'asc')
          sortDeals()}}
          className =" text-primary cursor-pointer"
        ><ArrowUpDown />
        </button>
      </div>
      <div className="mt-8 grid grid-cols-1 gap-4">
      {deals.map(deal => (
        <div key={deal.title} className="bg-dark rounded-xl p-5 shadow-sm">
          <h3 className="text-primary font-semibold">{deal.title}</h3>
          <div className="flex items-center gap-3 mt-2">
            <span className="bg-green text-green-text text-xs font-bold px-2 py-1 rounded">{deal.discount}</span>
            <span className="text-secondary text-sm line-through">{deal.original_price}</span>
            <span className="text-secondary text-sm">{deal.price}</span>
          </div>
        </div>
      ))}
      </div>
    </div>
    </div>
  )
}

export default App