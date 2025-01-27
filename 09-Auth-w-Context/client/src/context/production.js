import { createContext, useState, useContext } from 'react'

const ProductionContext = createContext()
// const ProductionContext = createContext({
//     productions: [],
//     setProductions: () => {}
// })
/* createContext takes an optional argument of a default value for if a component using this context is rendered outside of a ProductionProvider wrapper */ 

function ProductionProvider({ children }){

    const [productions, setProductions] = useState([])

    return (
        <ProductionContext.Provider value={{productions, setProductions}}>
            {children}
        </ProductionContext.Provider>
    )
}

const useProduction = () => {
    const context = useContext(ProductionContext)
    if (!context){
        throw new Error("useProduction must be used within a ProdutionProvider")
    }
    return context
}

export { ProductionProvider, useProduction }